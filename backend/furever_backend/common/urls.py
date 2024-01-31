from django.urls import path
from . import views

urlpatterns = [
    # <api/> will add into project/urls.py
    # '' -> http://127.0.0.1:8000/<api/>''
    path('institution_sign_up', view=views.sign_up_institution),
    path('pet_sign_up', view=views.sign_up_pet_from_institution),
    # custom url
]