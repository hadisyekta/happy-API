from rest_framework import serializers
from .models import Team, User, Happiness
from rest_framework.validators import UniqueForDateValidator
import datetime


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name', 'slug', 'is_active')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('is_active',)


class HappinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happiness
        fields = ('happiness_level', 'date', 'user')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Happiness.objects.all(),
                fields=('user', 'date'),
                message="Each user can add her/his level of happiness once time a day!"
            )
        ]
    date = serializers.DateField(initial=datetime.date.today)
    happiness_level = serializers.IntegerField(min_value=1, max_value=4)
