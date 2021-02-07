from django.shortcuts import render
from django.http import HttpResponse
from kit.models import Project, Kit
from products.models import Product

def home(request):
 projectsQuant = len(Project.objects.all())
 kitQuant = len(Kit.objects.all())
 productQuant = len(Product.objects.all())
 return render(request, 'index.html', {'Products': productQuant, 'Projects': projectsQuant, 'Kits': kitQuant})