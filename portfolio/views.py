from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Project, TechStack, SocialMedia, AboutMe, ContactMessage
from .forms import ContactForm

def home(request):
    about = AboutMe.objects.first()
    tech_stacks = TechStack.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    
    context = {
        'about': about,
        'tech_stacks': tech_stacks,
        'featured_projects': featured_projects,
    }
    return render(request, 'home.html', context)


def about(request):
    about = AboutMe.objects.first()
    social_media = SocialMedia.objects.all()
    
    context = {
        'about': about,
        'social_media': social_media,
    }
    return render(request, 'about.html', context)


def projects(request):
    all_projects = Project.objects.all()
    
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız uğurla göndərildi!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def download_cv(request):
    about = AboutMe.objects.first()
    if about and about.cv_file:
        try:
            return FileResponse(about.cv_file.open('rb'), content_type='application/pdf')
        except:
            raise Http404("CV tapılmadı")
    raise Http404("CV tapılmadı")