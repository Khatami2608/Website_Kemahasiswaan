# Generated by Django 3.2.18 on 2023-06-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0005_pelanggaran_prestasi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Beasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('dibuka', models.DateField()),
                ('ditutup', models.DateField()),
                ('benefit', models.TextField()),
                ('deskripsi', models.TextField()),
                ('persyaratan', models.TextField()),
                ('ip_minimal', models.IntegerField()),
                ('ipk_minimal', models.IntegerField()),
                ('status', models.TextField()),
                ('publikasi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]