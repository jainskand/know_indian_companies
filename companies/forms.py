from .models import UserSearches,CompanyDetail,Charges,Directors,CinModel
from django import forms
from . import scrap


class SearchCompanies(forms.Form):
    CIN = forms.CharField()

    def clean_CIN(self):
        cin=self.cleaned_data['CIN']
        if len(CinModel.objects.filter(CIN=cin))==0:
            msg = scrap.getalldata(cin)
            if msg!="success":
                raise forms.ValidationError(msg)
        return cin

class PreviousData(forms.Form):
    previuos = forms.ChoiceField()
