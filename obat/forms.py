from django import forms
from obat.models import Obat

class ObatForm(forms.ModelForm):
    class Meta:
        model = Obat
        fields = {
            'nama_obat',
            'deskripsi',
        }
