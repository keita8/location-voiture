from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'page/index.html'
    context = {
        
    }
    render(request, template_name, context)