from django.contrib import admin
from .models import Medecin, Patient, Pharmacie, Produit, Commande, Produit_Prescris, Admin, User, Ordonnance,PatientInfo

# Enregistrer tous les modèles dans l'interface d'administration
admin.site.register(Medecin)

admin.site.register(Pharmacie)
admin.site.register(PatientInfo)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Produit_Prescris)
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Ordonnance)
from django.contrib import admin
from .models import Patient
from .forms import PatientForm



admin.site.register(Patient)