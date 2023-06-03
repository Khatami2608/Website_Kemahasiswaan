import django_filters
from django import forms
from .models import *

class KegiatanFilter(django_filters.FilterSet):
    judul = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Judul',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cari Nama kegiatan'})
    )
    tanggal_publikasi = django_filters.DateFilter(
       	lookup_expr='icontains',
        label='Tanggal',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Format tanggal yang diterima (YYYY-MM-DD)
    )
    class Meta:
        model = kegiatan
        fields = ['judul', 'tanggal_publikasi']
