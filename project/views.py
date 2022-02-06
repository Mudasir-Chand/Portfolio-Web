from django.shortcuts import render, get_object_or_404
from .models import Project, About, Experience

# Create your views here.

def index(request):
    projects = Project.objects.all()
    abouts = About.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'projects' : projects,
        'abouts' : abouts,
        'experiences' : experiences
    }
    return render(request,'project/index.html', context)


def detail(request, project_id):
    
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project' : project
        
    }
    return render(request, 'project/detail.html',context)
