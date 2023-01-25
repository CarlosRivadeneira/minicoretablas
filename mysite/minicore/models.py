from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='productos')
    def __str__(self):
        return self.nombre