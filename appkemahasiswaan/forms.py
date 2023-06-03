from django.forms import ModelForm
from django import forms
from appkemahasiswaan.models import kegiatan

class FormKegiatan(ModelForm):
    class Meta:
        model = kegiatan
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'tanggal_publikasi': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'Deskripsi': forms.Textarea({'class': 'form-control'}),
            'image': forms.ClearableFileInput({'class': 'form-control'}),
        }

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Search'}))
