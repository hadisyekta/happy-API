from django.urls import path
from happyd1g1t import views
from happyd1g1t.views import HappinessCreationView, HappinessReportView

app_name = 'happyd1g1t'

urlpatterns = [
    path('apis', views.apiOverview, name="all_apis"),
    path('', HappinessCreationView.as_view({'post': 'create'}), name='happiness-create'),
    path('report/', HappinessReportView.as_view({'get': 'list'}), name='happiness-report'),
        # Get happiness report: if not authenticated: Average happiness of all teams
    #                      else: Average happiness of team and number of people in the same level
    ]