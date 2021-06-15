import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q, Avg, Sum

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TeamSerializer, HappinessSerializer
from .models import Happiness


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create': 'create/',
        'Details': 'details/<str:pk>',
        'All Happiness': '',
        'a:Statistic' : 'statistic/',
        'b:Average': 'allavg',
        'Happiness Per team': 'avg',
        'Today Happiness': 'todayavg',
    }

    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def HappinessList(request):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    happiness = Happiness.objects.all()
    serializer = HappinessSerializer(happiness, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def HappinessDetail(request, pk):

    try:
        happiness = Happiness.objects.get(id=pk)
    except Happiness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HappinessSerializer(happiness)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HappinessSerializer(happiness, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        happiness.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def HappinessCreate(request):
    serializer = HappinessSerializer(data=request.data)

    def happiness_create(self, serializer):
        serializer.save(user=self.request.user, team=self.request.user.employee.team, date=datetime.date.today())

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def HappinessAVGTeam(request):
    h = Happiness.objects.all()
    happiness_avg_perteam = Happiness.objects.values('team').annotate(happiness_avg_perteam=Avg('happiness_level')).order_by('-team')
    # happiness_avg_allteam = happiness_avg_perteam.aggregate(happiness_avg_allteam=Avg('happiness_avg_perteam'))
    # data = dict(happiness_avg_allteam= happiness_avg_allteam, happiness_avg_perteam=happiness_avg_perteam)
    return Response(happiness_avg_perteam)


@api_view(['GET'])
def HappinessAggregateAVG(request):
    h = Happiness.objects.all()
    today = datetime.date.today()
    happiness_avg_perteam2 = Happiness.objects.values('team').annotate(happiness_avg_perteam=Avg('happiness_level')).order_by('-team')
    happiness_avg_allteam2 = happiness_avg_perteam2.aggregate(happiness_avg_allteam=Avg('happiness_avg_perteam'))

    happiness_avg_perteam = Happiness.objects.select_related('user').values('user__team').annotate(happiness_avg_perteam=Avg('happiness_level')).order_by('-team')
    happiness_avg_allteam = happiness_avg_perteam.aggregate(happiness_avg_allteam=Avg('happiness_avg_perteam'))
    # data = dict(happiness_avg_allteam= happiness_avg_allteam, happiness_avg_perteam=happiness_avg_perteam)

    data = dict(happiness_avg_allteam= happiness_avg_allteam, happiness_avg_allteam2=happiness_avg_allteam2)
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def HappinessStat(request):
    # if user has not team what should I do?! how can I reais 404 without try catch?
    team = request.user.employee.team
    today = datetime.date.today()
    
    happiness_avg = Happiness.objects.filter(team=team, date=today).aggregate(happiness_avg=Avg('happiness_level'))
    # I filtered by day othewise I should find aggregation on each user for all days
    happiness_level_user_count = Happiness.objects.filter(team=team, date=today).values('happiness_level').annotate(user_count=Count('user')).order_by('-happiness_level')
    data = dict(happiness_level_user_count=happiness_level_user_count, happiness_avg=happiness_avg)

    happiness_avg_perteammate = Happiness.objects.filter(team=team).values('user').annotate(happiness_avg_peruser=Avg('happiness_level')).order_by('-user')
    print(happiness_avg_perteammate)
    data = dict(happiness_level_user_count=happiness_level_user_count, happiness_avg=happiness_avg, happiness_avg_perteammate=happiness_avg_perteammate)
    return Response(data)