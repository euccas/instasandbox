from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
  message = models.TextField()
  quote = models.TextField(blank=True, null=True)
  createDate = models.DateField(default=date.today)
  updateDate = models.DateTimeField(auto_now=True)