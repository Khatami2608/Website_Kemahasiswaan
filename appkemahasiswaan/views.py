from django.shortcuts import render
from appkemahasiswaan.models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import *
from django.core.paginator import Paginator
from .filters import *
from urllib.parse import urlencode

# MENU KEGIATAN
# Menampilkan data kegiatan

def DataKegiatanListView(request):
    ordering = '-tanggal_publikasi'
    keyword = request.GET.get('cari')  # Use GET instead of POST for search keyword
    cari_tgl = request.GET.get('cari_tgl')  # Change to 'cari_tgl'

    dt_kegiatan = kegiatan.objects.all()

    # Filter berdasarkan keyword
    if keyword:
        dt_kegiatan = dt_kegiatan.filter(judul__icontains=keyword)

    # Filter berdasarkan tanggal_publikasi
    if cari_tgl:
        dt_kegiatan = dt_kegiatan.filter(tanggal_publikasi__date=cari_tgl)  # Change to 'cari_tgl'

    # Ordering
    dt_kegiatan = dt_kegiatan.order_by(ordering)

    # Pagination
    paginator = Paginator(dt_kegiatan, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    dt_kegiatan = paginator.get_page(page_number)

    konteks = {
        'dt_kegiatan': dt_kegiatan,
    }

    return render(request, 'kegiatan/data-kegiatan.html', konteks)




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     myFilter = KegiatanFilter(self.request.GET, queryset=self.get_queryset())
    #     context['myFilter'] = myFilter

    #     # Mengambil parameter filter dari URL saat berpindah halaman
    #     filter_params = self.request.GET.dict()
    #     filter_params.pop('page', None)
    #     context['filter_params'] = urlencode(filter_params)

    #     return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     myFilter = KegiatanFilter(self.request.GET, queryset=queryset)
    #     return myFilter.qs

# Tambah kegiatan
def tambah_kegiatan(request):
    konteks = {}

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
            return render(request, 'kegiatan/tambah-kegiatan.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }

    else:
        form = FormKegiatan()

        konteks = {
            'form': form,
        }    
    return render(request, 'kegiatan/tambah-kegiatan.html', konteks)

# Proses ubah data kegiatan
def ubah_kegiatan(request, id_kegiatan):
    dt_kegiatan = kegiatan.objects.get(id=id_kegiatan)
    template = 'kegiatan/ubah-kegiatan.html'
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
# END KEGIATAN

# START VIEW UNTUK PRESTASI
def PrestasiView(request):
    nama = request.GET.get('carinama')
    ordering = request.GET.get('ordering', '-nama')
    form = FormPrestasi()
    prodi = request.GET.get('cariprodi')
    
    pretasi = Prestasi.objects.all()

    if nama:
        pretasi = pretasi.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama)
        )

    if prodi:
        pretasi = pretasi.filter(prodi=prodi)

    pretasi = pretasi.order_by(ordering)

    paginator = Paginator(pretasi, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    pretasi = paginator.get_page(page_number)

    konteks = {
        'form': form,
        'pretasi': pretasi,
        'nama': nama,
        'prodi': prodi,
        'ordering': ordering,
    }

    return render(request, 'prestasi/tabel-prestasi.html', konteks)
 

# Tambah Prestasi
def AddPrestasiView(request):
    form = FormPrestasi()
    pesan = ""

    if request.POST:
        form = FormPrestasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPrestasi()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'prestasi/tambah-prestasi.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }


    konteks = {
        'form': form,
        'pesan': pesan,
    }
    
    return render(request, 'prestasi/tambah-prestasi.html', konteks)

from django.shortcuts import redirect

def EditPrestasiView(request, nim_Prestasi):
    prestasi = Prestasi.objects.get(nim=nim_Prestasi)
    template = 'prestasi/Edit-prestasi.html'
    if request.POST:
        form = FormPrestasi(request.POST, request.FILES, instance=prestasi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_prestasi', nim_Prestasi=nim_Prestasi)
    else:
        form = FormPrestasi(instance=prestasi)
        konteks = {
            'form': form,
            'prestasi': prestasi,
        }
    return render(request, template, konteks)

# Proses Hapus data Kegiatan
def HapusPrstasiView(request, nim_Prestasi):
    prestasi = Prestasi.objects.filter(nim=nim_Prestasi)
    prestasi.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/prestasi/')

# END Prestasi
# Tambah data Pelanggaran
def AddPelanggaranView(request):
    form = FormPelanggaran()
    pesan = ""

    if form.is_valid():
        form.save()
        form = FormPelanggaran()
        pesan = "Data Berhasil Disimpan"

        konteks = {
            'form': form,
            'pesan': pesan,
        }
        return render(request, 'pelanggaran/tambah-pelanggaran.html', konteks)
    else:
        pesan2 = "Lengkapi data yang ada"

        konteks = {
            'form': form,
            'pesan2': pesan2,
        }


    konteks = {
        'form': form,
        'pesan': pesan,
    }
    return render(request, 'pelanggaran/tambah-pelanggaran.html', konteks)

# Tampilkan Data Pelanggaran
def PelanggaranView(request):
    nama = request.GET.get('carinama')
    ordering = '-publikasi'
    form = FormPelanggaran()
    prodi = request.GET.get('cariprodi')
    
    pelanggaran = Pelanggaran.objects.all()

    if nama:
        pelanggaran = pelanggaran.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama)
        )

    if prodi:
        pelanggaran = pelanggaran.filter(prodi=prodi)

    pelanggaran = pelanggaran.order_by(ordering)

    paginator = Paginator(pelanggaran, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    pelanggaran = paginator.get_page(page_number)

    konteks = {
        'form': form,
        'pelanggaran': pelanggaran,
        'nama': nama,
        'prodi': prodi,
        'ordering': ordering,
    }

    return render(request, 'pelanggaran/tabel-pelanggaran.html', konteks)

def EditPelanggaranView(request, nim_Pelanggaran):
    pelanggaran = Pelanggaran.objects.get(nim=nim_Pelanggaran)
    template = 'pelanggaran/Edit-pelanggaran.html'
    if request.POST:
        form = FormPelanggaran(request.POST, request.FILES, instance=pelanggaran)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_pelanggaran', nim_Pelanggaran=nim_Pelanggaran)
    else:
        form = FormPelanggaran(instance=pelanggaran)
        konteks = {
            'form': form,
            'pelanggaran': pelanggaran,
        }
    return render(request, template, konteks)

def HapusPelanggaranView(request, nim_pelanggaran):
    pelanggaran = Pelanggaran.objects.filter(nim=nim_pelanggaran)
    pelanggaran.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/pelanggaran/')

# START DATA BEASISWA
def AddDataBeasiswa(request):
    form = FormDataBeasiswa()
    pesan = ""

    if request.POST:
        form = FormDataBeasiswa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormDataBeasiswa()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Data_Beasiswa/AddData_Beasiswa.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    else:
        form = FormDataBeasiswa()

    konteks = {
        'form': form,
    }
    return render(request, 'Data_Beasiswa/AddData_Beasiswa.html', konteks)

def DataBeasiswa(request):
    nama = request.GET.get('carinama')
    ordering = '-publikasi'
    
    data_beasiswa = Data_Beasiswa.objects.all().order_by(ordering)

    if nama:
        data_beasiswa = data_beasiswa.filter(nama__icontains=nama)

    paginator = Paginator(data_beasiswa, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    data_beasiswa = paginator.get_page(page_number)

    konteks = {
        'data_beasiswa': data_beasiswa,
        'nama': nama,
        'ordering': ordering,
    }

    return render(request, 'Data_Beasiswa/data-beasiswa.html', konteks)

def Ubah_DataBeasiswa(request, id_Data_Beasiswa):
    data_beasiswa = Data_Beasiswa.objects.get(id=id_Data_Beasiswa)
    template = 'Data_Beasiswa/Ubah-DataBeasiwa.html'
    if request.POST:
        form = FormDataBeasiswa(request.POST, request.FILES, instance=data_beasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Ubah_DataBeasiswa', id_Data_Beasiswa=id_Data_Beasiswa)
    else:
        form = FormDataBeasiswa(instance=data_beasiswa)
        konteks = {
            'form': form,
            'data_beasiswa': data_beasiswa,
        }
    return render(request, template, konteks)

def Hapus_DataBeasiswa(request, id_Data_Beasiswa):
    data_beasiswa = Data_Beasiswa.objects.filter(id=id_Data_Beasiswa)
    data_beasiswa.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/Data-Beasiswa/')