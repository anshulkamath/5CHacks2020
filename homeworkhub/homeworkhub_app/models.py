from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
  name = models.CharField(max_length=100)
  students = models.ManyToManyField(User, through="BatSignal")

  # activeBatSignals = []
  # inactiveBatSignals = []
  # when a user first adds a course, they are added to list of inactive
  # when a user activates their bat signal, added to list of active

  def __str__(self):
    return self.name

class BatSignal(models.Model):
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
  active = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username + ' active in ' + self.course.name + '? ' + str(self.active)