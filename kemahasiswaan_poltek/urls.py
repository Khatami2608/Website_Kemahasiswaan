from django.conf import settings
from django.contrib import admin
from django.urls import path
from appkemahasiswaan.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data-kegiatan/', DataKegiatanListView, name='data_kegiatan'),
    path('tambah-kegiatan/', tambah_kegiatan, name='tambah_kegiatan'),
    path('data-kegiatan/page/<int:page>/', DataKegiatanListView, name='data_kegiatan_page'),
   	path('ubah-kegiatan/<int:id_kegiatan>/', ubah_kegiatan, name='ubah_kegiatan'),
    path('hapus-kegiatan/<int:id_kegiatan>/', hapus_kegiatan, name='hapus_kegiatan'),
    path('prestasi/', PrestasiView, name='prestasi'),
    path('tambah-prestasi/', AddPrestasiView, name='Addprestasi'),
    path('Edit-prestasi/<int:nim_Prestasi>/', EditPrestasiView, name='Edit_prestasi'),
    path('Hapus-prestasi/<int:nim_Prestasi>/', HapusPrstasiView, name='hapus_prestasi'),
    path('tambah-pelanggaran/', AddPelanggaranView, name='tambah_pelanggaran'),
    path('pelanggaran/', PelanggaranView, name='pelanggaran'),
    path('Edit-pelanggaran/<int:nim_Pelanggaran>/', EditPelanggaranView, name='Edit_pelanggaran'),
    path('Hapus-pelanggaran/<int:nim_pelanggaran>/', HapusPelanggaranView, name='hapus_pelanggaran'),
    path('Tambah-Data-Beasiswa/', AddDataBeasiswa, name='AddData_Beasiswa'),
    path('Data-Beasiswa/', DataBeasiswa, name='Data_Beasiswa'),
    path('Edit-Data-Beasiswa/<int:id_Data_Beasiswa>/', Ubah_DataBeasiswa, name='Ubah_DataBeasiswa'),
    path('hapus-DataBeasiswa/<int:id_Data_Beasiswa>/', Hapus_DataBeasiswa, name='Hapus_DataBeasiswa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
