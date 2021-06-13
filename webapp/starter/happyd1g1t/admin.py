from django.contrib import admin

# Register your models here.
from .models import User, Team, Happiness

   

class HappinessAdmin(admin.ModelAdmin):
     fields = ('happiness_level', 'user', 'date')



admin.site.register(User)
admin.site.register(Team)
admin.site.register(Happiness, HappinessAdmin)