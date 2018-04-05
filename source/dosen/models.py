from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dosen (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('pria', 'Laki-Laki'),
        ('wanita', 'Perempuan'),
    )

    # akun = models.ForeignKey(User,  on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=25)
    foto = models.FileField(null=True, blank=True)
    status = models.BooleanField(default=False)
    

    def __unicode__(self):
        return self.nama

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ["nama"]

class Akun (models.Model):
    JENIS_AKUN_CHOICES = (
        ('staf', 'Staf'),
        ('dosen', 'Dosen'),
        ('admin', 'Administrator'),
    )

    akun = models.ForeignKey(User,  on_delete=models.CASCADE)
    profil = models.ForeignKey(Dosen,  on_delete=models.CASCADE)
    jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)

    def __unicode__(self):
        return self.profil.nama

    def __str__(self):
        return self.profil.nama