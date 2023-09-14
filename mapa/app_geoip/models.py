from django.db import models

# Create your models here.

class IPLog(models.Model):
    ip = models.CharField(max_length=15)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    tempo = models.DateTimeField()
