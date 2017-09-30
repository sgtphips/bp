from django.shortcuts import render
from .models import Summary, Experience, School, Skill, Certification
# Create your views here.

def home(request):
	summary = Summary.objects.all()
	experience = Experience.objects.all()
	school = School.objects.all()
	skill = Skill.objects.all()
	certification = Certification.objects.all()
	return render(request, 'home/home.html', {'summary': summary, 'experience': experience, 'school': school, 'skill': skill, 'certification': certification})
