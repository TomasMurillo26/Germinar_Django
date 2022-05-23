from django.urls import path
from .views import principal, plantasInterior

urlpatterns = [
    path('', principal, name='principal'),
    path('', plantasInterior, name='plantasInterior'),
]