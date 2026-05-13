from django.shortcuts import (render)
from .models import Portfolio



# Create your views here.
def portfolio(request):
    projects = Portfolio.objects.all()
    return render(request, template_name= 'portfolio/portfolio.html', context={'projects':projects})

