from django.db import models

from django.contrib.auth.models import User as DjangoUser

# Create your models here.
class User(models.Model):
    auth = models.OneToOneField(DjangoUser)

    def __str__(self):
        return self.auth.username
