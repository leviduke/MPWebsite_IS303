from django.apps import AppConfig
from django.urls import path
from .views import indexPageView, missingpersonstable.html,
individualpersonpageview

urlpatterns = [  
    path("individualperson/", individualpersonPageView, 
name="idnividualperson"), 
    path("<str:oPerson>/", missingpersonPageView, name="mptable"), 
    path("", indexPageView, name="index"),
] 

class MpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mpapp'
