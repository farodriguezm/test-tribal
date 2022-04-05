from django.urls import path
from .views import ping, jokes

app_name = 'api'

urlpatterns = [
    path('ping', ping, name='ping'),
    path('jokes', jokes, name='jokes')
]
