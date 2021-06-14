from django.contrib import admin

from .models import Team, Happiness


class HappinessAdmin(admin.ModelAdmin):
     fields = ('happiness_level', 'user', 'date')

admin.site.register(Team)
admin.site.register(Happiness, HappinessAdmin)