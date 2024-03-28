from django.urls import path
from .views import home, clinica, farmacia, duvidas

urlpatterns = [
    path('', home),
    path('clinica/', clinica),
    path('farmacia/', farmacia),
    path('duvidas/', duvidas),
]    