from django.shortcuts import render, redirect
from .models import Project, Skill, Message
from .forms import ProjectForm, MessageForm, SkillForm

from django.contrib import messages

from django.db.utils import OperationalError

# format_list = [('', '(all)')]
# geom_type_list = [('', '(all)')]
# try:
#     format_list.extend([(i[0],i[0]) 
#         for i in Format.objects.values_list('name')])
#     geom_type_list.extend([(i[0],i[0]) 
#         for i in Geom_type.objects.values_list('name')])
# except OperationalError:
#     pass  
#         # happens when db doesn't exist yet, views.py should be
#         # importable without this side effect

# Create your views here.

def homePage(request):
    project = Project.objects.all()
    detailed_skills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
            messages.success(request, 'Your message was successfully sent.')


    context = {'project': project, 'skills': skills, 'detailed_skills': detailed_skills, 'form': form}
    return render(request, 'base/home.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)

    context = {'project': project}
    return render(request, 'base/project.html', context)

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    # adding the instance below will tell form what to update from
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)

def inboxPage(request):
    # messages that haven't been read top priority
    inbox = Message.objects.all().order_by('is_read')

    # unread
    unreadCount = Message.objects.filter(is_read=False).count()

    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'base/inbox.html', context)

def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()

    context = {'message': message}
    return render(request, 'base/message.html', context)

def addSkill(request):
    form = SkillForm()
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your skill was successfully sent.')
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/skill_form.html', context)