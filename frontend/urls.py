from django.urls import path

from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', HomeView, name='home'),
    path('profile/<int:id>', Profile, name='profile')
]
