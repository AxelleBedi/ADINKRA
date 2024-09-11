from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Commande

# Exemple de création de groupes et permissions
gestionnaires_stock = Group.objects.create(name='Gestionnaires de stock')
gestion_commandes = Group.objects.create(name='Gestion des commandes')

content_type = ContentType.objects.get_for_model(Commande)
permission = Permission.objects.create(
    codename='peut_gérer_commandes',
    name='Peut gérer les commandes',
    content_type=content_type,
)

gestion_commandes.permissions.add(permission)

# Create your models here.
