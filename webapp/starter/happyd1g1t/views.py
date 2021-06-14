from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q, Avg

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
        'All': '',
        'a:Statistic' : 'statistic/',
        'b:Average': 'avg',
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
        if serializer.is_valid():
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
        serializer.save(user=self.request.user)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def HappinessAVG(request):
    h = Happiness.objects.all()
    happy_avg_team = Happiness.objects.annotate(num_team=Count('team')).aggregate(Avg('happiness_level'))
    return Response(happy_avg_team)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def HappinessStat(request):
    happiness = Happiness.objects.all()
    
    serializer = HappinessSerializer(happiness, many=True)
    return Response(serializer.data)