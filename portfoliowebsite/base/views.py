from django.shortcuts import render
from .models import Project

# Create your views here.

def homePage(request):
    project = Project.objects.all()

    context = {'project': project}
    return render(request, 'base/home.html', context)