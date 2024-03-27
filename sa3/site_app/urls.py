from django.urls import path
from .views import home, clinica

urlpatterns = [
    path('', home),
    path('clinica/', clinica)
]    