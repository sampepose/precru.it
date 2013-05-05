from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import UserProfile

admin.site.register(Permission)
admin.site.register(UserProfile)

