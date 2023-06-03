from django.conf import settings
from django.contrib import admin
from django.urls import path
from appkemahasiswaan.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data-kegiatan/', DataKegiatanListView.as_view(), name='data_kegiatan'),
    path('tambah-kegiatan/', tambah_kegiatan, name='tambah_kegiatan'),
    path('data-kegiatan/page/<int:page>/', DataKegiatanListView.as_view(), name='data_kegiatan_page'),
    path('ubah-kegiatan/ubah/<int:id_kegiatan>/', ubah_kegiatan, name='ubah_kegiatan'),
    path('hapus-kegiatan/hapus/<int:id_kegiatan>/', hapus_kegiatan, name='hapus_kegiatan'),
    path('cari-kegiatan/', cari_kegiatan, name='cari_kegiatan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
