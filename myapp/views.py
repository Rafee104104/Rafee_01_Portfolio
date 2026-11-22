from .models import *
from django.shortcuts import render, redirect
from django.http import request
from .models import *
from django.contrib.auth import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # user.set_password(form.cleaned_data.get('password1')])
            profile = Profile.objects.create(user=user)
            profile.save()
            
            return redirect('signin')
    else:
        form = RegistrationForm()
    return render(request,'registrationform.html',{'form':form})

def signin(request):
    if request.method=="POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('homepage')
    else:
        form = LoginForm()

    return render(request,'loginForm.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('registration')

@login_required
def homepage(request):
    profile = Profile.objects.filter(user=request.user).first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'profile' :profile,
        'educations' : educations,
        'experiences' : experiences,
        'projects' : projects,
        'skills' : skills
    }
    return render(request,'homepage.html',context)


@login_required
def addProfile(request):
    if Profile.objects.filter(user=request.user).exists():
        return redirect('homepage')

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('homepage')
    else:
        form = ProfileForm()

    return render(request, 'addProfile.html', {'form': form})


@login_required
def editProfile(request,id):
    profile = Profile.objects.get(id=id)
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile,)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'editProfile.html',{'form':form})

@login_required
def deleteProfile(request,id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('homepage')


def addEducation(request):
    if request.method=="POST":
        form = EducationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EducationForm()

    return render(request,'addEducation.html',{'form':form})


@login_required
def editEducation(request,id):
    education = Education.objects.get(id=id)
    if request.method=="POST":
        form = EducationForm(request.POST,instance=education)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EducationForm(instance=education)
    return render(request,'editEducation.html',{'form':form})

@login_required
def deleteEducation(request,id):
    education = Education.objects.get(id=id)
    education.delete()
    return redirect('homepage')

@login_required
def addExperience(request):
    if request.method=="POST":
        form = ExperienceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExperienceForm()

    return render(request,'addExperience.html',{'form':form})


@login_required
def editExperience(request,id):
    experience = Experience.objects.get(id=id)
    if request.method=="POST":
        form = ExperienceForm(request.POST,instance=experience)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExperienceForm(instance=experience)
    return render(request,'editExperience.html',{'form':form})

@login_required
def deleteExperience(request,id):
    experience = Experience.objects.get(id=id)
    experience.delete()
    return redirect('homepage')


@login_required
def addProject(request):
    if request.method=="POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProjectForm()

    return render(request,'addProject.html',{'form':form})


@login_required
def editProject(request,id):
    project = Project.objects.get(id=id)
    if request.method=="POST":
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProjectForm(instance=project)
    return render(request,'editProject.html',{'form':form})

@login_required
def deleteProject(request,id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('homepage')

@login_required
def addSkill(request):
    if request.method=="POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SkillForm()

    return render(request,'addSkill.html',{'form':form})


@login_required
def editSkill(request,id):
    skill = Skill.objects.get(id=id)
    if request.method=="POST":
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SkillForm(instance=skill)
    return render(request,'editSkill.html',{'form':form})

@login_required
def deleteSkill(request,id):
    skill = Skill.objects.get(id=id)
    skill.delete()
    return redirect('homepage')

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

