from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='home'),
    path('events/', views.events, name='events')
]