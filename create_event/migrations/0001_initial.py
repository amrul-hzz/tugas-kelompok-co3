# Generated by Django 4.1 on 2022-11-02 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaEvent', models.CharField(max_length=255)),
                ('namaPantai', models.CharField(max_length=255)),
                ('alamatPantai', models.CharField(max_length=255)),
                ('jumlahPartisipan', models.IntegerField()),
                ('fotoPantai', models.URLField()),
                ('deskripsi', models.TextField()),
                ('tanggalMulai', models.DateField()),
                ('tanggalAkhir', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
