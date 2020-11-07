from django.shortcuts import render

def home(request):
  context = {
    "pagetitle": "hwh",
  }
  return render(request, 'homeworkhub_app/home.html', context)
