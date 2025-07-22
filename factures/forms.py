from django import forms
from .models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['titre', 'montant_ht', 'tva', 'categorie', 'client', 'paye']
