from django.contrib import admin

# Register your models here.
from phiauth.models import PhiUser

admin.site.register(PhiUser)
