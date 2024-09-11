from django.contrib import admin 
from django.urls import include, path 
from .views import index, catalogue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalogue/', catalogue, name='page_de_catalogue'),
    path('authentification/', include('authentification.urls', namespace='authentification')),  
    path('paiement/', include('paiement.urls',namespace='paiement')),
    path('espace_admin/',include('espace_admin.urls'))
]
