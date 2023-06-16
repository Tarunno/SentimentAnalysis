from django.urls import path
from . views import ApiOverView, Analyze

urlpatterns = [
    path('', ApiOverView, name='api_over_view'),
    path('analyze', Analyze, name="analyze"),
]
