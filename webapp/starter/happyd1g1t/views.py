import datetime

from django.db.models import Count, Avg

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import HappinessSerializer
from .models import Happiness


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All APIs': 'apis/',
        'Create': 'happiness/',
        'Happiness report': 'happiness/report',
    }

    return Response(api_urls)

class HappinessCreationView(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # TODO: add property user.is_employee
        try:
            team = request.user.employee.team
        except:
            return Response({'success': None, 
            'errors': 'You must be part of a team to insert level of your happiness.'})
        # TODO: Cleaner way of adding employee to request data
        data = {
            **request.data,
            'employee': request.user.employee.id
        }
        serializer = HappinessSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Your input has been accepted', 'errors': []})
        return Response({'success': None, 'errors': serializer.errors})


class HappinessReportView(viewsets.ViewSet):

    def get_allteam_average(self):
        today = datetime.date.today()
        happiness_avg_perteam = Happiness.objects.filter(date=today) \
        .select_related('employee') \
        .values('employee__team').order_by('-employee__team') \
        .annotate(happiness_avg_perteam=Avg('happiness_level')) \
        
        happiness_avg_allteam = happiness_avg_perteam \
        .aggregate(happiness_avg_allteam=Avg('happiness_avg_perteam'))

        return {'happiness_avg_allteam': happiness_avg_allteam}

    def get_myteam_report(self, happiness):
        team_happiness_avg = happiness.aggregate(happiness_avg=Avg('happiness_level'))

        happiness_level_user_count = happiness \
            .values('happiness_level') \
            .order_by('happiness_level') \
            .annotate(count=Count('happiness_level'))
        return {**team_happiness_avg, 'happiness_level_user_count': happiness_level_user_count}

    def list(self, request):
        if request.user.is_authenticated:

            try:
                team = request.user.employee.team
            except:
                return Response({'success': None, 
                'errors': 'You must be part of a team to insert level of your happiness.'})

            today = datetime.date.today()
            team = request.user.employee.team
            happiness = Happiness.objects.filter(employee__team=team, date=today)
            data = self.get_myteam_report(happiness)

        else:
            data = self.get_allteam_average()
        return Response({
                'data': data,
                'success': '',
                'errors': []})