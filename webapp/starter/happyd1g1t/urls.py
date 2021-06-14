from django.urls import path
from . import views

urlpatterns = [
    path('apis', views.apiOverview, name="all_apis"),
    path('', views.HappinessList, name="all-happiness"),
    path('create/', views.HappinessCreate, name="add-happiness"),
    path('details/<str:pk>', views.HappinessDetail, name="get-happiness"),
    path('allavg', views.HappinessAggregateAVG, name="allavg-happiness"),
    path('avg', views.HappinessAVGTeam, name="team-avg-happiness"),
    path('statistic', views.HappinessStat, name="stat-happiness")
]