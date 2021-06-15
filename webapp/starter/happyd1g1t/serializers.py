import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueForDateValidator

from .models import Employee, Team, Happiness, HappinessLevel

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'slug', 'is_active')

class EmployeeSerializer(serializers.ModelSerializer):
    team = TeamSerializer(required=True, allow_null=False)

    class Meta:
        model = Employee
        fields = ('team', 'user')

class HappinessSerializer(serializers.ModelSerializer):
    happiness_level = serializers.IntegerField(
        min_value=HappinessLevel.HIGHLY_UNSATISFACTORY,
        max_value=HappinessLevel.HIGHLY_SATISFACTORY
    )
    date = serializers.DateField(required=False, default=datetime.date.today())

    class Meta:
        model = Happiness
        fields = ('happiness_level', 'date', 'employee')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Happiness.objects.all(),
                fields=('employee', 'date'),
                message="Each employee can add her/his level of happiness once time a day!"
            )
        ]