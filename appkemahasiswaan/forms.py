from django.forms import ModelForm, forms
from django import forms
from appkemahasiswaan.models import *

class FormKegiatan(ModelForm):
    class Meta:
        model = kegiatan
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'tanggal_publikasi': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'Deskripsi': forms.Textarea({'class': 'form-control', 'placeholder': 'Tuliskan Deskripsi Kegiatan'}),
            'image': forms.ClearableFileInput({'class': 'form-control'}),
        }

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Search'}))

class FormPrestasi(ModelForm):
    class Meta:
        model = Prestasi
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'prestasi': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Prestasi Mahasiswa'}),
            'penyelenggara': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan penyelenggara'}),
            'tanggal': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'tingkat': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Tingkat Perlombaan'}),
            'juara': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Juara Ke-'}),
            'gender': forms.Select({'class': 'form-control'}),
        }

class FormPelanggaran(ModelForm):
    class Meta:
        model = Pelanggaran
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'angkatan': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Angkatan'}),
            'Jenis_pelanggaran': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Jenis Pelanggaran Yang Dilakukan'}),
            'sanksi': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Sanksi Yang di Dapatkan'}),
        }

class FormDataBeasiswa(ModelForm):
    class Meta:
        model = Data_Beasiswa
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Beasiswa'}),
            'dibuka': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'ditutup': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'benefit': forms.Textarea({'class': 'form-control', 'placeholder': 'Masukkan Benefit Yang Diterima'}),
            'deskripsi': forms.Textarea({'class': 'form-control', 'placeholder': 'Masukkan Deskripsi Beasiswa'}),
            'persyaratan': forms.Textarea({'class': 'form-control', 'placeholder': 'Masukkan Persyaratan Beasiswa'}),
            'ip_minimal': forms.NumberInput({'class': 'form-control', 'placeholder': 'IP Minimal '}),
            'ipk_minimal': forms.NumberInput({'class': 'form-control', 'placeholder': 'IPK Minimal '}),
            'status': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Status Beasiswa'}),
            'image': forms.ClearableFileInput({'class': 'form-control'}),
        }
