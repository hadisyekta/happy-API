from django.contrib import admin

# Register your models here.
from .models import User, Team

admin.site.register(User)
admin.site.register(Team)
