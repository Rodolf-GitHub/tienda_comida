from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class Producto(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to='imagenes/',null=True)
    descripcion=models.CharField(max_length=250)

    def __str__(self) -> str:
        fila="Nombre :"+self.nombre+"-"+"Descripcion :"+self.descripcion
        return fila
    def delete(self, using: None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        return super().delete()

class Orden(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    Codigo_del_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
