from django.urls import path
from . import views

urlpatterns = [
    # <api/> will add into project/urls.py
    # '' -> http://127.0.0.1:8000/<api/>''
    path('', view=views.getData),

    # custom url
    # 'api/institutions' -> http://127.0.0.1:8000/<api/institutions>
    path('api/institutions', view=views.getDatas),

]