
from django.urls import  include, path # type: ignore
from .views import dashboard


urlpatterns = [
    
    path('',dashboard,name='dash'),
    
   
    
    
]
