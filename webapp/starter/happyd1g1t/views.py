from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q

from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
def HappinessList(request):
    happiness = Happiness.objects.all()
    serializer = HappinessSerializer(happiness, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def HappinessDetail(request, pk):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
def HappinessCreate(request):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer = HappinessSerializer(data=request.data)

    def happiness_create(self, serializer):
        serializer.save(user=self.request.user)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def HappinessAVG(request):
    # h = Happiness.objects.all()
    h= Happiness.objects.raw('SELECT * FROM happyd1g1t_happiness  ')
    # q[0].entry__count
    print(h, "count", h[0], request.user, "level",  h[0].happiness_level)
    serializer = HappinessSerializer(h, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def HappinessStat(request):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    happiness = Happiness.objects.all()
    serializer = HappinessSerializer(happiness, many=True)
    return Response(serializer.data)