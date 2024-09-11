from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def mon_panier(request):
    # Récupérer les articles dans le panier de l'utilisateur (exemple simplifié)
    panier = request.session.get('panier', {})  # Récupérer le panier de la session
    total = sum(item['prix'] * item['quantité'] for item in panier.values())  # Calculer le total
    
    # Passer les données du panier au template
    context = {
        'panier': panier,
        'total': total,
    }
    return render(request, 'cart.html', context)

from django.shortcuts import render, redirect

@login_required(login_url="pageconnexion")
def finaliser_commande(request):
    if request.method == 'POST':
        # Traitez les informations de la commande ici (paiement, adresse de livraison, etc.)
        commande = {
            'adresse': request.POST.get('adresse'),
            'mode_paiement': request.POST.get('mode_paiement'),
             'numéro_telephone': request.POST.get('numéro_telephone'),
            # Ajouter d'autres champs nécessaires
        }
        # Enregistrez la commande, videz le panier, etc.
        request.session['panier'] = {}  # Vider le panier après finalisation
        return redirect('historique')  # Rediriger vers l'historique des commandes
    
    # Si c'est une requête GET, afficher le formulaire de finalisation
    return render(request, 'finaliser_commande.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def historique(request):
    # Récupérer les commandes de l'utilisateur connecté
    commandes = []  # Remplacez par une requête pour récupérer les commandes de l'utilisateur
    context = {
        'commandes': commandes,
    }
    return render(request, 'historique.html', context)

