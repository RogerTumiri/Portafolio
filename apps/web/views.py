from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class index(TemplateView):
    template_name = 'index.html' 

class contact(TemplateView):
    template_name = 'contact.html'

class projects(TemplateView):
    template_name = 'projects.html'

class resume(TemplateView):
    template_name = 'resume.html'
