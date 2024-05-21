# Generated by Django 5.0.4 on 2024-05-21 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('spesifikasi', models.TextField()),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hps', to='tokohp.kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Penjualan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('jumlah', models.PositiveIntegerField()),
                ('total_harga', models.DecimalField(decimal_places=2, max_digits=12)),
                ('hp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penjualan', to='tokohp.hp')),
            ],
        ),
    ]
