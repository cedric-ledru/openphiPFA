from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    # owner of document in databases
    auth = models.ForeignKey(User)
    content = models.TextField()
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title
