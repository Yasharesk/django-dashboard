from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample, oursample, area

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]