
from django.contrib import admin
from django.urls import include, path
from app import views 
urlpatterns = [
   
    path('pagedegarde/', views.page_de_garde, name='pagedegarde'),  # Chemin pour accéder à votre page de garde
    path('pharmacie/', views.pharmacie, name='pharmacie'),
    path('a_propos_de_nous/', views.a_propos, name='apropos'),
    path('contact/', views.contact, name='contact'),
    path('administrateur/', views.admin, name='administrateur'),
    path('medecin/', views.medecin, name='medecin'),
    path('authentification/', views.authentification, name='authentification'),
       path('connexion/', views.connexion, name='connexion'),
    path('connexion/inscription_patient.html', views.inscription_patient, name='inscription_patient'),
    path('connexion/inscription_pharmacie.html', views.inscription_pharmacie, name='inscription_pharmacie'),
    path('connexion/inscription_medecin.html', views.inscription_medecin, name='inscription_medecin'),
    path('connexion/inscription_livreur.html', views.inscription_livreur, name='inscription_livreur'),
   # path('valider_ordonnance/', views.valider_ordonnance, name='valider_ordonnance'),
    
    
   
]
