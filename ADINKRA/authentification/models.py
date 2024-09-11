from django.db import models # type: ignore
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin # type: ignore
from django.utils import timezone # type: ignore
from django.core.mail import send_mail # type: ignore
from django.conf import settings # type: ignore
from django.template.loader import render_to_string # type: ignore

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email doit être défini")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Les superutilisateurs doivent avoir is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Les superutilisateurs doivent avoir is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def send_password_reset_email(self):
        """Envoie un email de réinitialisation de mot de passe."""
        mail_subject = "Réinitialisation de votre mot de passe"
        template = "authentification/mot_de_passe_oub.html"
        context = {"user": self, "date": timezone.now().date()}
        send_mail(
            mail_subject,
            render_to_string(template, context),
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
            html_message=render_to_string(template, context),
        )
