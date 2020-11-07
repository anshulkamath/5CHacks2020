from django.shortcuts import render
from .models import Course, BatSignal

def home(request):
  context = {
    "pagetitle": "HH // Home",
    "courses": Course.objects.all()
  }
  return render(request, 'homeworkhub_app/home.html', context)

def courses(request):
  context = {
    "pagetitle": "HH // Courses",
    "courses": Course.objects.all(),
    "batSignals": BatSignal.objects.all()
  }
  return render(request, 'homeworkhub_app/courses.html', context)
