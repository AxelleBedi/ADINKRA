from django.contrib import admin 
from django.urls import  include, path
from .views import mon_panier,finaliser_commande,historique 

app_name = 'paiement'
urlpatterns = [
    
path('',mon_panier,name='page_panier'), # type: ignore
path('finaliser_commande/',finaliser_commande,name='commande'),
path('historique_commande/',historique,name='historique'),

     ]
