from django.urls import path
from .views import uniform_distribution


urlpatterns = [
    path('', uniform_distribution, name='uniform_distribution'),
]
