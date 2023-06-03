from django.shortcuts import render
from appkemahasiswaan.models import *
from .forms import FormKegiatan
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import *
from django.core.paginator import Paginator
from .filters import *
from urllib.parse import urlencode

# MENU KEGIATAN
# Menampilkan data kegiatan
class DataKegiatanListView(ListView):
    model = kegiatan
    template_name = 'data-kegiatan.html'
    context_object_name = 'dt_kegiatan'
    ordering = ['-tanggal_publikasi']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myFilter = KegiatanFilter(self.request.GET, queryset=self.get_queryset())
        context['myFilter'] = myFilter

        # Mengambil parameter filter dari URL saat berpindah halaman
        filter_params = self.request.GET.dict()
        filter_params.pop('page', None)
        context['filter_params'] = urlencode(filter_params)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        myFilter = KegiatanFilter(self.request.GET, queryset=queryset)
        return myFilter.qs

def cari_kegiatan(request):
    myFilter = KegiatanFilter(request.GET, queryset=kegiatan.objects.all())
    dt_kegiatan = myFilter.qs

    konteks = {
        'dt_kegiatan': dt_kegiatan,
        'myFilter': myFilter,
    }
    return render(request, 'data-kegiatan.html', konteks)

# Tambah kegiatan
def tambah_kegiatan(request):
    if request.POST:
        form = FormKegiatan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKegiatan()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-kegiatan.html', konteks)

    else:
        form = FormKegiatan()

        konteks = {
            'form': form,
        }    
    return render(request, 'tambah-kegiatan.html', konteks)

# Proses ubah data kegiatan
def ubah_kegiatan(request, id_kegiatan):
    dt_kegiatan = kegiatan.objects.get(id=id_kegiatan)
    template = 'ubah-kegiatan.html'
    if request.POST:
        form = FormKegiatan(request.POST, request.FILES, instance=dt_kegiatan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('ubah_kegiatan', id_kegiatan=id_kegiatan)
    else:
        form = FormKegiatan(instance=dt_kegiatan)
        konteks = {
            'form': form,
            'dt_kegiatan': dt_kegiatan,
        }
    return render(request, template, konteks)

# Proses Hapus data Kegiatan
def hapus_kegiatan(request, id_kegiatan):
    dt_kegiatan = kegiatan.objects.filter(id=id_kegiatan)
    dt_kegiatan.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/data-kegiatan/')

# Fungsi untuk mencari data kegiatan
def cari_kegiatan(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        dt_kegiatan = kegiatan.objects.filter(nama_kegiatan__icontains=keyword)
        konteks = {
            'dt_kegiatan': dt_kegiatan,
            'keyword': keyword,
        }
        return render(request, 'data-kegiatan.html', konteks)
    else:
        return redirect('/data-kegiatan/')
# END KEGIATAN

# VIEW UNTUK PRESTASI
#def DataPrestasi(request):


