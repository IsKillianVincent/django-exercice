from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_factures, name='liste_factures'),
    path('facture/ajouter/', views.creer_facture, name='creer_facture'),
    path('facture/<int:pk>/', views.detail_facture, name='detail_facture'),
    path('facture/<int:pk>/modifier/', views.modifier_facture, name='modifier_facture'),
    path('facture/<int:pk>/supprimer/', views.supprimer_facture, name='supprimer_facture'),
]
