import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueForDateValidator

from .models import Employee, Team, Happiness, HAPPINESS_LEVEL


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'slug', 'is_active')

class HappinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happiness
        fields = ('happiness_level', 'date', 'user', 'team')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Happiness.objects.all(),
                fields=('user', 'date'),
                message="Each user can add her/his level of happiness once time a day!"
            )
        ]
    date = serializers.DateField(initial=datetime.date.today)
    happiness_level = serializers.IntegerField(min_value=HAPPINESS_LEVEL.HIGHLY_UNSATISFACTORY, max_value=HAPPINESS_LEVEL.HIGHLY_SATISFACTORY)
