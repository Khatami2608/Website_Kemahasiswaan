from django.contrib import admin
from appkemahasiswaan.models import *

# MODEL UNTUK KEGIATAN.
class kegiatanAdmin(admin.ModelAdmin):
	list_display = ['judul', 'tanggal_publikasi', 'Deskripsi', 'image']
	search_fields = ['judul', 'tanggal_publikasi']
	list_per_page = 5
	readonly_fields=[
		'tanggal_publikasi',
		'slug',
		'update',
	]
admin.site.register(kegiatan, kegiatanAdmin)
admin.site.register(Prodi)
admin.site.register(Agama)
admin.site.register(Gender)

# MODEL UNTUK MAHASISWA
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'prodi', 'agama', 'gender']
    search_fields = ['nim', 'nama']
    list_filter = ['prodi']

admin.site.register(Mahasiswa, MahasiswaAdmin)

class PrestasiAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'prodi', 'prestasi', 'tingkat', 'publikasi']
    search_fields = ['nim', 'nama']
    list_filter = ['prodi']

admin.site.register(Prestasi, PrestasiAdmin)

class PelanggaranAdmin(admin.ModelAdmin):
	list_display = ['nim', 'nama', 'prodi', 'angkatan', 'Jenis_pelanggaran', 'sanksi', 'publikasi']
	search_fields = ['nim', 'nama']
	list_filter = ['prodi']

admin.site.register(Pelanggaran, PelanggaranAdmin)

class DataBeasiswaAdmin(admin.ModelAdmin):
	readonly_fields=[
		'publikasi',
	]

admin.site.register(Data_Beasiswa, DataBeasiswaAdmin)
