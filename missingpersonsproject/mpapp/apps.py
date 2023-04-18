from django.apps import AppConfig
from django.urls import path
from .views import indexPageView, missingpersonstablePageView, individualpersonPageView, displayPersonPageView


urlpatterns = [  
    path("individualperson/", individualpersonPageView, name="idnividualperson"), 
    path("<str:oPerson>/", missingpersonstablePageView, name="mptable"), 
    path("", indexPageView, name="index"),
] 

class MpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mpapp'
