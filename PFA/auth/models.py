from django.db import models

from django.contrib.auth.models import User as DjangoAuthUser


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(DjangoAuthUser)

    def __str__(self):
        return self.user.username
