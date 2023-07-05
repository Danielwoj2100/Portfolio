from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Project, Language, Skill, Link, Education, Experience, Technology


# Create your views here.

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})


def index(request):
    projects = Project.objects.all().order_by('-creationDate')
    return render(request, 'index.html', {'projects': projects})


def CV(request):
    return render(request, 'CV.html')


def about(request):
    languages = Language.objects.all()
    skills = Skill.objects.all()
    links = Link.objects.all()
    educations = Education.objects.all()
    experience = Experience.objects.all()
    return render(request, 'AboutMe.html',
                  {'languages': languages, 'skills': skills, 'links': links, 'educations': educations,
                   'experience': experience})


def tech_projects(request, technology):
    try:
        tech_object = Technology.objects.get(technologies=technology)
        projects = Project.objects.filter(technologies=tech_object).order_by('-creationDate')
        message = None
    except ObjectDoesNotExist:
        projects = []
        message = "The requested technology isn't used in any of the listed projects"

    return render(request, 'index.html', {'projects': projects, 'message': message})
