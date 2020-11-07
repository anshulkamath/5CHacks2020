from django.shortcuts import render
from .models import Course

def home(request):
  context = {
    "pagetitle": "hwh",
    "courses": Course.objects.all()
  }
  return render(request, 'homeworkhub_app/home.html', context)
