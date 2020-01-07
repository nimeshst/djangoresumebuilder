# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserDetailForm
from .forms import ExperienceForm
from .forms import EducationForm
from .forms import SkillsForm
from .forms import HobbiesForm
from .forms import LanguagesForm
from .forms import ProjectForm

def home(request):
	return render(request,"resumebuilder/home.html")

def UserDetails(request):
	if request.method == 'POST':
		# save the the form data in the database
		form = UserDetailForm(request.POST)
		if form.is_valid():
			# save the form data 
			form = form.save(commit = False)
			form.user = request.user
			form.save(commit = True)
			redirect('/experience/')
	else:
		form = UserDetailForm()
	return render(request, "resumebuilder/userdetails.html", {'form':form})

def experience(request):
	form = ExperienceForm()
	return render(request,"resumebuilder/experience.html",{'form':form})

def education(request):
	form = EducationForm()
	return render(request,"resumebuilder/education.html",{'form':form})

def skills(request):
	form = SkillsForm()
	return render(request, "resumebuilder/skills.html",{'form':form})

def project(request):
	form = ProjectForm()
	return render(request, "resumebuilder/project.html",{'form':form})

def extracurricular(request):
	hobbies_form = HobbiesForm()
	languages_form = LanguagesForm()
	return render(request, "resumebuilder/extracurricular.html",{'hobbies_form':hobbies_form,'languages_form':languages_form})