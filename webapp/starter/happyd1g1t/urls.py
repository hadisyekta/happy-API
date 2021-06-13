from django.urls import path
from . import views

urlpatterns = [
    path('add_happiness/', view.HappinessCreate, name="add-happiness"),
    path('happiness/<str:pk>', view.HappinessDetail, name="get-happiness"),
    path('all_happiness/', view.HappinessList, name="all-happiness")
]