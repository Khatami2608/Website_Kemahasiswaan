# Generated by Django 3.2.18 on 2023-06-03 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0003_agama_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('nim', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('angkatan', models.IntegerField()),
                ('alamat', models.TextField()),
                ('no_tlp', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('agama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.agama')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.gender')),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.prodi')),
            ],
        ),
    ]
