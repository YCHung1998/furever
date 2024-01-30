from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    # info from institutions/admin.py class MyAdminSite
    default_site = "furever_backend.admin.MyAdminSite" 