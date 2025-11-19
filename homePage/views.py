from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import QuerySet

# Create your views here.


class homeView(TemplateView):
    template_name = 'homePage/home.html'
    def get_context_data(self, **a):
        context = super().get_context_data(**a)
        context['school'] = "naresh it"
        return context
