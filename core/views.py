from django.shortcuts import render, HttpResponse

from core import migrations

#Create your views here.
def base(request):
    return render(request, template_name='core/base.html')
def home(request):
    return render(request, template_name='core/home.html')
def about(request):
    return render(request, template_name='core/about.html')
def contacto(request):
    return render(request, template_name='core/contacto.html')
