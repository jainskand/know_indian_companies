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
    previuos = forms.ChoiceField(label='Previous Data  :')

    def __init__(self, cin,*args, **kwargs):
        super(PreviousData, self).__init__(*args, **kwargs)
        d = CinModel.objects.filter(CIN=cin).order_by('-create_date')
        self.fields['previuos'].choices = [(i.id,i.create_date) for i in d]
