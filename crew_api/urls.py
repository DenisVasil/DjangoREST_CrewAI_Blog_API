from django.urls import path
from .views import CrewProcessView

urlpatterns = [
    path('', CrewProcessView.as_view(), name='crew_process'),
]
