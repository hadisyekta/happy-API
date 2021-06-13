from rest_framework import serializers
from .models import Team, User, Happiness


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