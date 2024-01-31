from django.urls import path, include
from . import views

urlpatterns = [
    #  we will add url into project/urls.py and add the app name
    # so the uel path will become
    # http://~/institution/...
    path('CRUD/', view=views.institutions_list),
    path('<int:id>', view=views.institution_detail),

]
