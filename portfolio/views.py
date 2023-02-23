from django.shortcuts import render
from portfolio.models import proyectos

# Create your views here.

def portfolio(request):
   portfolio = proyectos.objects.all()

   return render(request, "proyectos/portfolio.html", {"portfolio": portfolio})