


from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .utils import create_sex_pie_chart, create_age_bar_chart
from .models import PatientInfo
def page_de_garde(request):
    return render(request, 'pagegarde.html')


def pharmacie(request):
    return render(request, 'pharmacie.html')
def a_propos(request):
    return render(request, 'apropos.html')
def contact(request):
    return render(request, 'formulairecontact.html')
def admin(request):
    return render(request, 'administrateur.html')
def medecin(request):
    return render(request, 'medecin.html')
def authentification(request):
    return render(request, 'authentification.html')
def connexion(request):
    return render(request, 'connexion.html')
def inscription_patient(request):
    return render(request, 'inscription_patient.html')
def inscription_pharmacie(request):
    return render(request, 'inscription_pharmacie.html')
def inscription_medecin(request):
    return render(request, 'inscription_medecin.html')
def inscription_livreur(request):
    return render(request, 'inscription_livreur.html')


from .models import Patient

from django.http import HttpResponse, HttpResponseBadRequest

#def valider_ordonnance(request):
   # if request.method == 'POST':
        # Récupérer les données du formulaire d'ordonnance
      #  id_medecin = request.POST.get('id_medecin')
       # id_patient = request.POST.get('id_patient')
       # nom_patient = request.POST.get('nom_patient')
       # age_patient = request.POST.get('age_patient')
        #sexe_patient = request.POST.get('sexe_patient')

        # Créer une nouvelle instance de PatientInfo
        #patient_info = PatientInfo(
          #  nom=nom_patient,
           # age=age_patient,
           # sexe=sexe_patient
            # Ajoutez d'autres champs si nécessaire
       # )

        # Enregistrez les données dans la base de données
       # patient_info.save()
       # create_sex_pie_chart()
       # create_age_bar_chart()
        # Retourner un message de confirmation
       # message_confirmation = 'validée avec succès.'
       # return HttpResponse(message_confirmation)
    #else:
        #return HttpResponseBadRequest('Méthode non autorisée.')


