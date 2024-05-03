from django.db import models

class HP(models.Model):
    nama = models.CharField(max_length=100)
    spesifikasi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class HP1Jutaan(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    hp = models.ForeignKey(HP, on_delete=models.CASCADE, related_name='hp_1jutaan')

    def __str__(self):
        return self.nama

class HP2Jutaan(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    hp = models.ForeignKey(HP, on_delete=models.CASCADE, related_name='hp_2jutaan')

    def __str__(self):
        return self.nama
