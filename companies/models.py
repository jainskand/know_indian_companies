from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.

class UserSearches(models.Model):
    CIN  = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    companySearched = models.ForeignKey('CinModel',on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.CIN+' '+self.user.username
    def isupdated(self):
         return timezone.now() < self.create_date + timezone.timedelta(days=15)

class CinModel(models.Model):
    CIN  = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.CIN
    def isupdated(self):
        return timezone.now() < self.create_date + timezone.timedelta(days=15)


class CompanyDetail(models.Model):
    user  = models.OneToOneField('CinModel',on_delete=models.CASCADE,related_name='companydetail')
    CIN = models.CharField(max_length=200)
    CompanyName = 	models.CharField(max_length=200)
    ROCCode	= models.CharField(max_length=200,null=True)
    RegistrationNumber	 = models.CharField(max_length=200,null=True)
    CompanyCategory	= models.CharField(max_length=200,null=True)
    CompanySubCategory = models.CharField(max_length=200,null=True)
    ClassofCompany = models.CharField(max_length=200,null=True)
    AuthorisedCapital = models.FloatField(null=True)
    PaidupCapital = models.FloatField(null=True)
    NumberofMembers = models.IntegerField(null=True)
    DateofIncorporation	= models.DateTimeField(null=True)
    RegisteredAddress =	models.CharField(max_length=500,null=True)
    AddressotherthanRo =  models.CharField(max_length=500,null=True)
    EmailId	 = models.EmailField(max_length=254, null=True)
    WhetherListed =	models.CharField(max_length=200,null=True)
    ACTIVEcompliance = models.CharField(max_length=200,null=True)
    Suspendedatstockexchange = models.CharField(max_length=200,null=True)
    DateoflastAGM = models.DateTimeField(null=True)
    DateofBalanceSheet = models.DateTimeField(null=True)
    CompanyStatus  = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.CompanyName

class Charges(models.Model):
    company  = models.ForeignKey('CompanyDetail',on_delete=models.CASCADE,related_name='charges',null=True)
    llp  = models.ForeignKey('LLPDetails',on_delete=models.CASCADE,related_name='charges',null=True)
    foreigncompany  = models.ForeignKey('ForeignCompanyDetail',on_delete=models.CASCADE,related_name='charges',null=True)
    Assetsundercharge = models.CharField(max_length=500,null=True)
    ChargeAmount = models.FloatField(null=True)
    DateofCreation = models.DateTimeField(null=True)
    DateofModification = models.DateTimeField(null=True)
    Status = models.CharField(max_length=200,null=True)

class Directors(models.Model):
    company  = models.ForeignKey('CompanyDetail',on_delete=models.CASCADE,related_name='directors',null=True)
    llp  = models.ForeignKey('LLPDetails',on_delete=models.CASCADE,related_name='directors',null=True)
    foreigncompany  = models.ForeignKey('ForeignCompanyDetail',on_delete=models.CASCADE,related_name='directors',null=True)
    DIN = models.CharField(max_length=200,null=True)
    Name = models.CharField(max_length=200,null=True)
    Begindate = models.DateTimeField(null=True)
    Enddate = models.DateTimeField(null=True)
    SurrenderedDIN  = models.CharField(max_length=200,null=True)


class LLPDetails(models.Model):
    user  = models.OneToOneField('CinModel',on_delete=models.CASCADE,related_name='llpdetail')
    LLPIN = models.CharField(max_length=200, null=True)
    LLPName	= models.CharField(max_length=400, null=True)
    NumberofPartners = models.IntegerField(null=True)
    NumberofDesignatedPartners = models.IntegerField(null=True)
    ROCCode	= models.CharField(max_length=200, null=True)
    DateofIncorporation = models.DateTimeField(null=True)
    RegisteredAddress = models.CharField(max_length=500, null=True)
    EmailId	= models.EmailField(max_length=254, null=True)
    Previousfirm = models.CharField(max_length=400, null=True)
    TotalObligationofContribution = models.FloatField(null=True)
    MaindivisionofbusinessactivityinIndia = models.CharField(max_length=200, null=True)
    Descriptionofmaindivision = models.CharField(max_length=500, null=True)
    DateofAccountsSolvencyfiled	= models.DateTimeField(null=True)
    DateofAnnualReturnfiled	= models.DateTimeField(null=True)
    LLPStatus = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.LLPName


class ForeignCompanyDetail(models.Model):
    user  = models.OneToOneField('CinModel',on_delete=models.CASCADE,related_name='foreigncompanydetail')
    FCRN = models.CharField(max_length=200, null=True)
    CompanyName	= models.CharField(max_length=400, null=True)
    DateofIncorporation = models.DateTimeField(null=True)
    CountryofIncorporation = models.CharField(max_length=200, null=True)
    RegisteredAddress = models.CharField(max_length=500, null=True)
    EmailId = models.EmailField(max_length=254, null=True)
    ForeignCompanywithShareCapital = models.CharField(max_length=200, null=True)
    CompanyStatus = models.CharField(max_length=200, null=True)
    TypeofOffice =	models.CharField(max_length=200, null=True)
    Details	= models.CharField(max_length=500, null=True)
    MaindivisioninIndia	= models.CharField(max_length=200, null=True)
    Descriptionofmaindivision = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.CompanyName
