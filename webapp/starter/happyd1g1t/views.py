from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, HappinessSerializer
from .models import Happiness


@api_view(['GET'])
def HappinessList(request):
    happiness = Happiness.objects.all()
    serializer = HappinessSerializer(happiness, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def HappinessDetail(request, pk):
    happiness = Happiness.objects.get(id=pk)
    serializer = HappinessSerializer(happiness)
    return Response(serializer.data)

@api_view(['POST'])
def HappinessCreate(request):
    serializer = HappinessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)