from django.shortcuts import render, HttpResponse

from core.models import Persona


#Create your views here.
def base(request):
    return render(request, template_name='core/base.html')
def home(request):
    return render(request, template_name='core/home.html')
def about(request):
    return render(request, template_name='core/about.html')
def contacto(request):
    persona = Persona.objects.first()  # 1 registro o None
    return render(request, "core/contacto.html", {"persona": persona})


