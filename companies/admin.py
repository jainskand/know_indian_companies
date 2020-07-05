from django.contrib import admin
from .models import UserSearches,CompanyDetail,Charges,Directors,CinModel,ForeignCompanyDetail,LLPDetails
# Register your models here.
admin.site.register(UserSearches)
admin.site.register(CompanyDetail)
admin.site.register(Charges)
admin.site.register(Directors)
admin.site.register(CinModel)
admin.site.register(ForeignCompanyDetail)
admin.site.register(LLPDetails)
