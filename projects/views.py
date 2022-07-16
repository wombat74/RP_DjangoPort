from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

def all_projects(request):
    # query db to return all projects objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})
