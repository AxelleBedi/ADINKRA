from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Commande,Produit

def dashboard(request):
    # Obtenir des statistiques
    total_ventes = Commande.objects.filter(status='Livré').count()
    total_revenus = Commande.objects.filter(status='Livré').aggregate(Sum('montant_total'))
    produits_populaires = Produit.objects.order_by('-ventes')[:5]
    commandes_en_attente = Commande.objects.filter(status='En attente').count()

    # Contexte à passer au template
    context = {
        'total_ventes': total_ventes,
        'total_revenus': total_revenus['montant_total__sum'] if total_revenus['montant_total__sum'] else 0,
        'produits_populaires': produits_populaires,
        'commandes_en_attente': commandes_en_attente,
    }
    return render(request, 'dashboard.html', context)


# Create your views here.
