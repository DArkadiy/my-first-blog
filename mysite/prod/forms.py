from django import forms

from .models import Zakaz, Detal

class ZakazForm(forms.ModelForm):

    class Meta:
        model = Zakaz
        fields = ('nom_zak','title', 'text','start_date','finish_date','status')

class DetalForm(forms.ModelForm):

    class Meta:
        model = Detal
        fields = ('detal_title', 'detal_size','detal_weight','detal_text','detal_status')

