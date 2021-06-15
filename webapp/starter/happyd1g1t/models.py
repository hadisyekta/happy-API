import uuid
import datetime
from django.db import models

from django.contrib.auth.models import User

class HappinessLevel:
    HIGHLY_UNSATISFACTORY = 1
    MOSTLY_UNSATISFACTORY = 2
    SOMEWHAT_UNSATISFACTORY = 3
    UNSATISFACTORY = 4
    NEUTRAL = 5
    SATISFACTORY = 6
    SOMEWHAHT_SATISFACTORY = 7
    MODERATELY_SATISFACTORY = 8
    MOSTLY_SATISFACTORY = 9
    HIGHLY_SATISFACTORY = 10

    choices = [
        (HIGHLY_UNSATISFACTORY,'Highly Unsatisfactory'), 
        (MOSTLY_UNSATISFACTORY,  'Mostly Unsatisfactory'), 
        (SOMEWHAT_UNSATISFACTORY, 'Somewhat Unsatisfactory'),
        (UNSATISFACTORY, 'Unsatisfactory'),
        (NEUTRAL, 'Neutral'), 
        (SATISFACTORY, 'Satisfactory'), 
        (SOMEWHAHT_SATISFACTORY, 'Somewhat Satisfactory'), 
        (MODERATELY_SATISFACTORY, 'Moderately Satisfactory'), 
        (MOSTLY_SATISFACTORY, 'Mostly Satisfactory'),
        (HIGHLY_SATISFACTORY, 'Highly Satisfactory'), 
    ]


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        name= self.user.first_name + " " + self.user.last_name if self.user.first_name else self.user.username          
        return str(name)
    


class Happiness(models.Model):
    happiness_level = models.IntegerField(
        default=HappinessLevel.NEUTRAL,
        choices=HappinessLevel.choices
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.date.today, blank=True, null=True)

    class Meta:
        ordering = ['date']
        unique_together = ('employee', 'date')

    def __str__(self):
        return str(self.happiness_level)
    