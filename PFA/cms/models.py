from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=100)
    path = models.FileField(upload_to="%Y/%m/%d")
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title
