from django.shortcuts import render,redirect,get_object_or_404
from .models import UserSearches,CompanyDetail,Charges,Directors,CinModel,ForeignCompanyDetail,LLPDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import scrap
from django.http import HttpResponse,Http404
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView
from .forms import SearchCompanies
from django import forms
from datetime import datetime
# Create your views here.

@login_required
def companyPage(request,cin,uid=None):

    #cin=slug
    #c = get_object_or_404(CinModel, CIN=cin)
    if uid!=None:
        c = get_object_or_404(UserSearches, pk=uid)
        if c.user!=request.user:
            raise Http404("Not authenticated")
        c=c.companySearched
    else:
        get_object_or_404(CinModel, CIN=cin)
        c = CinModel.objects.filter(CIN=cin).order_by('create_date')[0]

        cc = UserSearches(CIN=cin,user=request.user,companySearched=c)
        cc.save()

    t = c.type
    if t == 'company':
        companydata = c.companydetail
    elif t== 'llp':
        companydata = c.llpdetail
    elif t== 'foreigncompany':
        companydata = c.foreigncompanydetail
    context={
        'type' : c.type,
        'companydata' : companydata ,
    }

    return render(request,'companies/companydetail.html',context=context)

class SeachesListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'recentsearches'

    model = UserSearches
    context_object_name = 'allsearches'
    template_name = 'companies/usersearches.html'
    def get_queryset(self):
        return UserSearches.objects.filter(user__exact=self.request.user).order_by('-create_date')

@login_required
def companySearchView(request):
    form=SearchCompanies()
    if request.method == 'POST':
        form = SearchCompanies(request.POST)
        if form.is_valid():
            cin = form.cleaned_data['CIN']
            if len(CinModel.objects.filter(CIN=cin))==0:
                storedata(request,cin)
            print('working')
            t=False
            return redirect('companies:companydetail',cin=cin)
    return render(request,'companies/search_page.html',{'form':form})



@login_required
def storedata(request,cin):
    #scrap.getalldata(cin)

    comdir = scrap.getDirectors()
    comchar = scrap.getCharges()
    companytype = scrap.getType()

    cinentry  = CinModel(CIN = cin,type=companytype)
    cinentry.save()

    #cc = UserSearches(CIN=cin,user=request.user,companySearched=cinentry)
    #cc.save()

    comp=foreign=cllp=None

    if companytype == 'company':
        print("dataaa")
        comdet = scrap.getCompanyDetails()
        cd = CompanyDetail(user = cinentry,
                            CIN = comdet[0],
                            CompanyName = comdet[1],
                            ROCCode	= comdet[2],
                            RegistrationNumber	 = comdet[3],
                            CompanyCategory	= comdet[4],
                            CompanySubCategory = comdet[5],
                            ClassofCompany = comdet[6],
                            AuthorisedCapital = comdet[7],
                            PaidupCapital = comdet[8],
                            NumberofMembers = comdet[9],
                            DateofIncorporation	= comdet[10],
                            RegisteredAddress =	comdet[11],
                            AddressotherthanRo =  comdet[12],
                            EmailId	 = comdet[13],
                            WhetherListed =	comdet[14],
                            ACTIVEcompliance = comdet[15],
                            Suspendedatstockexchange = comdet[16],
                            DateoflastAGM = comdet[17],
                            DateofBalanceSheet = comdet[18],
                            CompanyStatus=comdet[19])
        cd.save()
        comp = cd

    elif companytype == 'llp':
        llpdta = scrap.getLlpDetails()
        cd = LLPDetails( user = cinentry,
                         LLPIN = llpdta[0],
                         LLPName = llpdta[1],
                         NumberofPartners = llpdta[2],
                         NumberofDesignatedPartners = llpdta[3],
                         ROCCode	= llpdta[4],
                         DateofIncorporation = llpdta[5],
                         RegisteredAddress = llpdta[6],
                         EmailId	= llpdta[7],
                         Previousfirm = llpdta[8],
                         TotalObligationofContribution = llpdta[9],
                         MaindivisionofbusinessactivityinIndia = llpdta[10],
                         Descriptionofmaindivision = llpdta[11],
                         DateofAccountsSolvencyfiled	= llpdta[12],
                         DateofAnnualReturnfiled	= llpdta[13],
                         LLPStatus = llpdta[14])
        cd.save()
        cllp=cd
    elif companytype == 'foreigncompany':
        fcdata = scrap.getForeignCompanyDetails()
        cd = ForeignCompanyDetail(user = cinentry,
                                  FCRN = fcdata[0],
                                  CompanyName	= fcdata[1],
                                  DateofIncorporation = fcdata[2],
                                  CountryofIncorporation = fcdata[3],
                                  RegisteredAddress = fcdata[4],
                                  EmailId = fcdata[5],
                                  ForeignCompanywithShareCapital = fcdata[6],
                                  CompanyStatus = fcdata[7],
                                  TypeofOffice = fcdata[8],
                                  Details	= fcdata[9],
                                  MaindivisioninIndia	= fcdata[10],
                                  Descriptionofmaindivision = fcdata[11])
        cd.save()
        foreign = cd

    Charges.objects.bulk_create([Charges(company  = comp,
                                         foreigncompany=foreign,
                                         llp = cllp,
                        Assetsundercharge = com[0],
                        ChargeAmount = com[1],
                        DateofCreation = com[2],
                        DateofModification = com[3],
                        Status = com[4]) for com in comchar  ])
    '''for com in comchar:
        chrge = Charges(company  = cd,
                    Assetsundercharge = com[0],
                    ChargeAmount = com[1],
                    DateofCreation = com[2],
                    DateofModification = com[3],
                    Status = com[4])
        chrge.save()

    for direc in comdir:
        comd = Directors(company  = cd,
            DIN = direc[0],
            Name = direc[1],
            Begindate = direc[2],
            Enddate = direc[3],
            SurrenderedDIN  =direc[4])
        comd.save()'''
    Directors.objects.bulk_create([Directors(company  = comp,
                                         foreigncompany=foreign,
                                         llp = cllp,
        DIN = direc[0],
        Name = direc[1],
        Begindate = direc[2],
        Enddate = direc[3],
        SurrenderedDIN  =direc[4]) for direc in comdir])
