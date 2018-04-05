from __future__ import unicode_literals
from django import forms
from django.conf import settings

from django.db import models
from dosen.models import Dosen

# Create your models here.
class Kehadiran(models.Model):
    JENIS_KEHADIRAN_CHOICES = (
        ('sibuk', 'Sibuk'),
        ('senggang', 'Senggang'),
        ('pulang', 'Pulang'),
        ('ttd', 'TTD'),
    )

    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICES)
    tanggal = models.DateField()
    waktu_Mulai = models.TimeField()
    waktu_Selesai = models.TimeField()
    keterangan = models.TextField()
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.dosen.nama

    def __str__(self):
        return self.dosen.nama
    
    class Meta:
        ordering = ["tanggal"]