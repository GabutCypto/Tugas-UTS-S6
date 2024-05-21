from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nama

class HP(models.Model):
    nama = models.CharField(max_length=100)
    spesifikasi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey('Kategori', on_delete=models.SET_NULL, null=True, related_name='hps')

    def __str__(self):
        return self.nama

class Penjualan(models.Model):
    hp = models.ForeignKey(HP, on_delete=models.CASCADE, related_name='penjualan')
    tanggal = models.DateField(auto_now_add=True)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Penjualan {self.hp.nama} - {self.tanggal}"
