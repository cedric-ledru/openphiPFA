from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class PhiUser(models.Model):
    auth = models.OneToOneField(User)

    def __str__(self):
        return self.auth.username
