from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('recentsearches/',views.SeachesListView.as_view(),name='recentsearches'),
    path('companydetail/<slug:cin>/', views.companyPage,name='companydetail'),
    path('search/',views.companySearchView,name='searchpage'),
    path('companydetails/<slug:cin>/<int:uid>/', views.companyPage,name='companydetails'),
]
