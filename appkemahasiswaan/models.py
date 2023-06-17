from django.db import models
from PIL import Image
from django.utils.text import slugify

# DATABASE KEGIATAN
class kegiatan(models.Model):
	judul = models.CharField(max_length=225)
	tanggal_publikasi = models.DateTimeField(auto_now_add=True)
	Deskripsi = models.TextField()
	image = models.ImageField(upload_to='covers/', null=True)
	update = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):
		url_slug = {'slug':self.slug}
		return reverse('kegiatan:detail', kwargs = url_slug)

	def __str__(self):
	 	return self.judul 

class Prodi(models.Model):
    prodi = models.CharField(max_length=100)

    def __str__(self):
        return self.prodi

class Agama(models.Model):
    agama = models.CharField(max_length=100)

    def __str__(self):
        return self.agama

class Gender(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender

class Mahasiswa(models.Model):
    nim = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=100)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    angkatan = models.IntegerField()
    alamat = models.TextField()
    agama = models.ForeignKey(Agama, on_delete=models.CASCADE)
    no_tlp = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nim)

class Prestasi(models.Model):
    nim = models.IntegerField()
    nama = models.CharField(max_length=160)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    prestasi = models.CharField(max_length=100)
    penyelenggara = models.CharField(max_length=225)
    tanggal = models.DateField()
    tingkat = models.CharField(max_length=50)
    juara = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class Pelanggaran(models.Model):
    nim = models.IntegerField()
    nama = models.CharField(max_length=160)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    angkatan = models.IntegerField()
    Jenis_pelanggaran = models.CharField(max_length=300)
    sanksi = models.CharField(max_length=300)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nim

class Data_Beasiswa(models.Model):
    nama = models.CharField(max_length=200)
    dibuka =  models.DateField()
    ditutup = models.DateField()
    benefit = models.TextField()
    deskripsi = models.TextField()
    persyaratan = models.TextField()
    ip_minimal = models.IntegerField()
    ipk_minimal = models.IntegerField()
    status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='covers/', null=True)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama





