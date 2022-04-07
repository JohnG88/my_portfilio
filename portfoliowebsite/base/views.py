from django.shortcuts import render
from .models import Project, Skill

# Create your views here.

def homePage(request):
    project = Project.objects.all()
    detailed_skills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    context = {'project': project, 'skills': skills, 'detailed_skills': detailed_skills}
    return render(request, 'base/home.html', context)

def projectPage(request, pk):

    context = {}
    return render(request, 'base/project.html', context)