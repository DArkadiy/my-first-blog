from django import forms

from .models import Zakaz

class ZakazForm(forms.ModelForm):

    class Meta:
        model = Zakaz
        fields = ('nom_zak','title', 'text','start_date','finish_date','status')