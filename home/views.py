from django.shortcuts import render
from .models import Summary

# Create your views here.

def home(request):
	summary = Summary.objects.all()
	return render(request, 'home/home.html', {'summary': summary})
