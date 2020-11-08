from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
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

def updateActive(request, pk):
  context = {
    "pagetitle": "HH // Courses",
    "courses": Course.objects.all(),
    "batSignals": BatSignal.objects.all()
  }
  bs = BatSignal.objects.get(pk=pk)
  bs.active = True
  bs.save()
  return render(request, 'homeworkhub_app/courses.html', context)

def deactivateActive(request, pk):
  context = {
    "pagetitle": "HH // Courses",
    "courses": Course.objects.all(),
    "batSignals": BatSignal.objects.all()
  }
  bs = BatSignal.objects.get(pk=pk)
  bs.active = False
  bs.save()
  return render(request, 'homeworkhub_app/courses.html', context)

def addCourse(request, pk1, pk2):
  context = {
    "pagetitle": "HH // Courses",
    "courses": Course.objects.all(),
    "batSignals": BatSignal.objects.all()
  }
  course = Course.objects.get(pk=pk1)
  user = User.objects.get(pk=pk2)
  signal = BatSignal(user=user, course=course, active=False)
  signal.save()
  messages.success(request, 'You\'ve marked yourself active for {}!'.format(course.name))
  return render(request, 'homeworkhub_app/courses.html', context)
