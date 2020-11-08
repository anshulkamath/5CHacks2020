from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first = models.CharField(max_length=20, default='')
  last = models.CharField(max_length=20, default='')
  phone_number = models.CharField(max_length=11)

  def __str__(self):
    return 'Profile: {} {} ({})'.format(self.first, self.last, self.user.username)
