from django.db import models

# Create your models here.

class Facultate(models.Model):
    nume = models.CharField(max_length = 255)
    descriere = models.TextField()
    rating = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    oameni_pe_loc = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    locatie = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "facultati"
    

