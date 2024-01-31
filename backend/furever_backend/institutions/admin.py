from django.contrib import admin

# Register your models here.
from .models import Institution

class MyAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"

admin_site = MyAdminSite(name="institution_admin")
admin_site.register(Institution)