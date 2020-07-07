from .models import UserSearches,CompanyDetail,Charges,Directors,CinModel
from django import forms
from . import scrap
import re

class SearchCompanies(forms.Form):
    CIN = forms.CharField(label='CIN/FCRN/LLPIN :')

    def clean_CIN(self):
        cin=self.cleaned_data['CIN']
        cin = cin.upper()
        r=r"^[A-Z]{3}-[0-9]{4}$|^[F]{1}[0-9]{5}$|^[LU]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}"
        if re.match(r,cin)!=None:
            if len(CinModel.objects.filter(CIN=cin))==0:
                msg = scrap.getalldata(cin)
                if msg!="success":
                    raise forms.ValidationError(msg)
        else:
            raise forms.ValidationError('Enter Valid CIN/FCRN/LLPIN')
        return cin

class PreviousData(forms.Form):
    previuos = forms.ChoiceField(label='Previous Data  :')

    def __init__(self, cin,*args, **kwargs):
        super(PreviousData, self).__init__(*args, **kwargs)
        d = CinModel.objects.filter(CIN=cin).order_by('-create_date')
        self.fields['previuos'].choices = [(i.id,i.create_date) for i in d]
