from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse

class MonAdminSite(admin.AdminSite):
    site_header = "Gestion E-commerce"
    site_title = "Admin E-commerce"
    index_title = "Bienvenue dans l'administration"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view))
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        return HttpResponseRedirect(reverse('dashboard'))

admin_site = MonAdminSite(name='monadmin')

