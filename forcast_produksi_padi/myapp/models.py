# from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Prediction(models.Model):
    tahun = models.IntegerField()
    jumlah_produksi = models.IntegerField()

