from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='homeworkhub_home'),
    path('courses', views.courses, name='courses'),
    path('updateActive/<pk>/', views.updateActive, name='update_active'),
    path('deupdateActive/<pk>/', views.deactivateActive, name='update_deactive'),
    path('addCourse/<int:pk1>/<int:pk2>/', views.addCourse, name='addCourse'),
]