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

# MODEL UNTUK MAHASISWA
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'nama', 'prodi_mhs']  # Menggunakan 'get_prodi' sebagai metode yang mengembalikan prodi

    def get_prodi(self, obj):
        return obj.prodi

    prodi_mhs.short_description = 'Prodi'


# MODEL UNTUK PRESTASI MAHASISWA
class PrestasiAdmin(admin.ModelAdmin):
    list_display = ['nim_mhs', 'nama', 'prodi_id', 'prestasi', 'penyelenggara', 'tanggal', 'tingkat', 'juara']
    search_fields = ['NIM__NIM', 'nama']  # Menambahkan prefix NIM__ untuk mencari berdasarkan NIM
    list_per_page = 8

    def get_prodi(self, obj):
        return obj.prodi

    prodi_id.short_description = 'Prodi'


admin.site.register(Mahasiswa, MahasiswaAdmin)
admin.site.register(Prestasi, PrestasiAdmin)
admin.site.register(Prodi)