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
	nama = models.CharField(max_length=100)

	def __str__():
		return self.nama

# DATABASE MAHASISWA
class Mahasiswa(models.Model):
    NIM = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=100)
    prodi_mhs = models.ForeignKey(Prodi, on_delete=models.CASCADE, null=True)
    angkatan = models.IntegerField()
    alamat = models.TextField()
    agama = models.CharField(max_length=50)
    no_tlp = models.IntegerField()
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)

    def __str__(self):
    	return self.NIM

# DATABASE PRESTASI MAHASISWA
class Prestasi(models.Model):
	nim_mhs = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)
	nama = models.CharField(max_length=100)
	prodi_id = models.ForeignKey(Prodi, on_delete=models.CASCADE, null=True)
	prestasi = models.CharField(max_length=100)
	penyelenggara = models.CharField(max_length=100)
	tanggal = models.DateField()
	tingkat = models.CharField(max_length=50)
	juara = models.IntegerField()

	def __str__(self):
	    return self.nama




