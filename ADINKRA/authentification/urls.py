from django.contrib import admin  # type: ignore
from django.urls import  include, path # type: ignore
from .views import change_password, deco,connexion, inscription,  notif, password_reset_request

app_name = 'authentification'
urlpatterns = [
    
    path('',connexion,name='pageconnexion'),
    path('inscription/',inscription,name='pageinscription'),
    path("new_passe/",password_reset_request,name='new_passe'),
    path("changer/", change_password, name='changer_mdp'),
    path("page/",notif,name="notif"),
    path("deco/",deco,name="deco"),
 
   
    
    
]
