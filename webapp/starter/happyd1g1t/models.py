import uuid
import datetime
from django.db import models

from django.contrib.auth.models import User

class HAPPINESS_LEVEL:
    HIGHLY_UNSATISFACTORY= 1
    MOSTLY_UNSATISFACTORY= 2
    SOMEWHAT_UNSATISFACTORY = 3
    UNSATISFACTORY = 4
    NEUTRAL = 5
    SATISFACTORY = 6
    SOMEWAHT_SATISFACTORY = 7
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
        (SOMEWAHT_SATISFACTORY, 'Somewhat Satisfactory'), 
        (MODERATELY_SATISFACTORY, 'Moderately Satisfactory'), 
        (MOSTLY_SATISFACTORY, 'Mostly Satisfactory'),
        (HIGHLY_SATISFACTORY, 'Highly Satisfactory'), 
    ]

class Team(models.Model):
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    members = models.ManyToManyField(User)
    is_active = models.BooleanField(default=False)
    @property
    def team_happiness_level(self):
        members_count = self.members.count
        happiness_level = self.members.count
        return happiness_level / members_count 

    # def get_members_happiness(self):



class Happiness(models.Model):
    class Meta:
        ordering = ['happiness_level']
        unique_together = ('user', 'date')

    def __str__(self):
        return str(self.happiness_level)

    happiness_level = models.IntegerField(default=HAPPINESS_LEVEL.NEUTRAL, choices=HAPPINESS_LEVEL.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField("Date", default=datetime.date.today)