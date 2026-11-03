from django.db import models

# Create your models here.
#1 Categoria(id, nombre, descripcion)
class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()

    def __str__(self):
        return self.nombre

#2 Lugar Patrimonial (id, nombre, descripcion, ubicacion, año construccion, imagen, categoria(fk))
class LugarPatrimonial(models.Model):
    nombre=models.CharField(max_length=150)
    descripcion=models.TextField()
    ubicacion=models.CharField(max_length=150)
    anio_construccion=models.IntegerField()
    imagen=models.URLField(max_length=500)

    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre  
