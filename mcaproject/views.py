from  django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'index.html'

class Aboutpage(TemplateView):
    template_name = 'about.html'
