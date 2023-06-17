# Generated by Django 3.2.18 on 2023-06-09 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0004_mahasiswa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField()),
                ('nama', models.CharField(max_length=160)),
                ('prestasi', models.CharField(max_length=100)),
                ('penyelenggara', models.CharField(max_length=225)),
                ('tanggal', models.DateField()),
                ('tingkat', models.CharField(max_length=50)),
                ('juara', models.IntegerField()),
                ('publikasi', models.DateTimeField(auto_now_add=True)),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.gender')),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.prodi')),
            ],
        ),
        migrations.CreateModel(
            name='Pelanggaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField()),
                ('nama', models.CharField(max_length=160)),
                ('angkatan', models.IntegerField()),
                ('Jenis_pelanggaran', models.CharField(max_length=300)),
                ('sanksi', models.CharField(max_length=300)),
                ('publikasi', models.DateTimeField(auto_now_add=True)),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.prodi')),
            ],
        ),
    ]