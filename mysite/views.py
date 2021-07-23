from django.shortcuts import render
from loja.models import Project


def home(request):
  project = Project.objects.all()
  return render(request, 'index.html', {'projects':project})
