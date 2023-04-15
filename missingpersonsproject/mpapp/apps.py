from django.apps import AppConfig
from django.urls import path
from .views import indexPageView, missingpersonstable.html,

class MpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mpapp'
