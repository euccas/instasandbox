from django.db import models
from django.urls import reverse

from datetime import date

# Create your models here.
class Post(models.Model):
  message = models.TextField()
  quote = models.TextField(blank=True, null=True)
  createDate = models.DateField(default=date.today)
  updateDate = models.DateTimeField(auto_now=True)

  def get_absolute_url(self):
    return reverse("post", kwargs={"pk": self.pk})
    #return reverse("post", args=[str(self.id)])
  