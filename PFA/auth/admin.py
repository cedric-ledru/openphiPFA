from django.contrib import admin

# Register your models here.
from auth.models import OpenphiUser

admin.site.register(OpenphiUser)
