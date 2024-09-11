from django.shortcuts import render, HttpResponse, redirect # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash # type: ignore
from django.contrib.auth.hashers import check_password # type: ignore
from .forms import PasswordResetForm
from authentification.models import CustomUser # type: ignore
import logging
from django.core.mail import send_mail # type: ignore
from django.template.loader import render_to_string # type: ignore
from django.conf import settings # type: ignore
from datetime import datetime
from django.contrib.auth import get_user_model # type: ignore


logger = logging.getLogger(__name__)
User = get_user_model()



def index2(request):
    return render(request,'index2.html')

from .forms import InscriptionForm

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            # Vérifiez si l'utilisateur existe déjà
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Le nom d'utilisateur est déjà utilisé.")
            else:
                # Créez un nouvel utilisateur
                user = CustomUser.objects.create_user(username=username, email=email, password=mot_de_passe)
                messages.success(request, "Inscription réussie. Vous pouvez vous connecter.")
                return redirect('index')  # Redirection vers la page de connexion
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', {'form': form})



def connexion(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        mot_de_passe = request.POST.get('mot_de_passe')

        if nom and mot_de_passe:
            # Essayer d'authentifier l'utilisateur avec le modèle User de Django
            utilisateur = authenticate(request, username=nom, password=mot_de_passe)
            if utilisateur is not None:
                login(request, utilisateur)
                
                return redirect('index')   # Redirection vers la page après connexion

            # Si l'authentification échoue pour le modèle User
            messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrect.")
        else:
            messages.error(request, "Veuillez remplir tous les champs du formulaire.")

    return render(request, 'formulaire_connexion.html')

def deco(request): 
    logout(request)
    return redirect('index')
    
    


def send_email_with_html_body(
        subjet: str, receivers: list, template: str, context: dict
):
    """This fonction help to send a customize email to a specific user or set of users."""
    try:
        message = render_to_string(template, context)

        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message,
        )
        return True


    except Exception as e:
        logger.error(e)
    return False


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["email"]
            user = User.objects.get(email=data)

            mail_subject = "Réinitialisation de votre mot de passe"
            template = "authentification/mot_de_passe_oub.html"
            context = {"user": user, "date": datetime.today().date}

            receivers = [data]
            # message = f'bonjour {user.first_name} connectez vous avec ce mot de passe { mdp }  et en suite rendez-vous sur votre tableau de bord pour definir un nouveau mot de passe'
            send_email_with_html_body(
                subjet=mail_subject,
                receivers=receivers,
                template=template,
                context=context,
            )

            return redirect("notif")
    else:
        form = PasswordResetForm()
    return render(request, "new_mot_de_passe.html", {"form": form})


def notif(request):
    return render(request, "page_null.html")


def change_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)

        user.set_password(password)
        user.save()
        messages.success(request, "Mot de passe changé avec succès.")
        return render(request, 'index2.html')  # Redirigez vers une autre page comme un profil

    return render(request, "changer_mdp.html")















