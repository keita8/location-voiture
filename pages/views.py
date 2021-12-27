from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    template_name = 'home/index.html'
    context = {}
    
    return render(request, template_name, context)

def about(request):

    template_name = 'home/about.html'
    context = {}
    
    return render(request, template_name, context)


def contact(request):
    template_name = 'home/contact.html'
    context = {

    }

    return render(request, template_name, context)


def service(request):
    template_name = 'home/service.html'
    context = {

    }

    return render(request, template_name, context)
    
    