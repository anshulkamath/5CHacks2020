from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='homeworkhub_home'),
    path('courses', views.courses, name='courses'),
]