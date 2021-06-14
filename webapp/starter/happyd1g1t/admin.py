from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Team, Happiness, Employee

class HappinessAdmin(admin.ModelAdmin):
     fields = ('happiness_level', 'user', 'date')

admin.site.register(Team)
admin.site.register(Happiness, HappinessAdmin)

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)