from django.db import models
from django.db.models import F

# Create your models here.
class Tuman(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class IjtimoiyHimoya(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Person(models.Model):
    ism = models.CharField(max_length=200)
    familiya = models.CharField(max_length=200)
    otasining_ismi = models.CharField(max_length=200)
    passport_seriya = models.CharField(max_length=200)
    tuman = models.CharField(max_length=200, null=True)
    hozirgi_yashash_manzili = models.CharField(max_length=500, null=True)
    kimga_murojaat_qilgan = models.CharField(max_length=200)
    ijtimoiy_himoya = models.CharField(max_length=200, null=True)
    nogironligi = models.CharField(max_length=50, null=True)
    nogironlik_raqami = models.CharField(max_length=20, null=True)
    mablag_ajratgan_tashkilot = models.CharField(max_length=400)
    summa = models.BigIntegerField()
    photo = models.ImageField(upload_to='images', blank=True)
    tavsif = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.otasining_ismi} | {self.passport_seriya}"

    class Meta:
        ordering = [F('created').desc()]
