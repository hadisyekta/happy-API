from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Team, Happiness, Employee


@admin.display(description='Employee')
def employee_name(obj):
    user = obj.employee.user

    if user.first_name or user.last_name:
        return f'{user.first_name} {user.last_name}'
    return user.username


class HappinessAdmin(admin.ModelAdmin):
     fields = ('happiness_level', 'employee', 'date',)
     list_display = (employee_name, 'happiness_level', 'date',)


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