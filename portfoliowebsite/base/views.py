from django.shortcuts import render
from .models import Project, Skill
from .forms import ProjectForm

# Create your views here.

def homePage(request):
    project = Project.objects.all()
    detailed_skills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    context = {'project': project, 'skills': skills, 'detailed_skills': detailed_skills}
    return render(request, 'base/home.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)

    context = {'project': project}
    return render(request, 'base/project.html', context)

def addProject(request):
    form = ProjectForm()

    context = {'form': form}
    return render(request, 'base/project_form.html', context)