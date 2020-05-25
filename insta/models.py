from django.db import models

from datetime import date

# Create your models here.
class Post(models.Model):
  createDate = models.DateField(default=date.today)
  updateTime = models.DateTimeField(auto_now=True)
  message = models.TextField(blank=False, null=False)
  quote = models.TextField(blank=True, null=True)
