from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom_patient', 'sexe', 'date_naissance', 'num_tel', 'adresse']