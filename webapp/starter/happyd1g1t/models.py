from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime

PLEASURE = 1
PASSION = 2
PURPOSE = 3
ULTIMATE_GOOD = 4

class User(AbstractBaseUser):
    
    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    email = models.EmailField(unique=True, verbose_name='email address', max_length=255)
    full_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'full_name']

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


class Happiness(models.Model):
    class Meta:
        ordering = ['happiness_level']

    def __str__(self):
        return self.level

    HAPPINESS_LEVEL = (
        (PLEASURE, 'Pleasure'),
        (PASSION, 'Passion'),
        (PURPOSE, 'Purpose'),
        (ULTIMATE_GOOD, 'Ultimate Good'),
    )

    happiness_level = models.IntegerField(default=0, choices=HAPPINESS_LEVEL)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField("Date", default=datetime.date.today)