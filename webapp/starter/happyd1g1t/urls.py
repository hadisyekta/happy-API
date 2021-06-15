from django.urls import path
from . import views
from .views import HappinessCreationView, HappinessReportView

urlpatterns = [
    path('apis', views.apiOverview, name="all_apis"),
    # path('', views.HappinessList, name="all-happiness"),
    # path('create/', views.HappinessCreate, name="add-happiness"),
    # path('details/<str:pk>', views.HappinessDetail, name="get-happiness"),
    # path('allavg', views.HappinessAggregateAVG, name="allavg-happiness"),
    # path('avg', views.HappinessAVGTeam, name="team-avg-happiness"),
    # path('statistic', views.HappinessStat, name="stat-happiness"),


    path('', HappinessCreationView.as_view({'post': 'create'}), name='happiness-create'),
    path('report/', HappinessReportView.as_view({'get': 'list'})),
        # Get happiness report: if not authenticated: Average happiness of all teams
    #                      else: Average happiness of team and number of people in the same level
    ]