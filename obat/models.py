from django.db import models
from registrasi.models import Pasien, Dokter

class Obat(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.DO_NOTHING)
    dokter = models.ForeignKey(Dokter, on_delete=models.DO_NOTHING)
    tanggal = models.DateField()
    nama_obat = models.CharField(max_length=16)
    deskripsi = models.TextField()