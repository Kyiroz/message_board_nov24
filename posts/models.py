from django.db import models

# Create your models here.

#Aqui creamos las tablas (el nombre de la tabla debe entenderse)
class Publication(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()#Puede tener la cantidad de texto necesaria

#Cuando se agrega un dato, el dato agregado aparecera con su titulo en la tabla
    def __str__(self) -> str:
        return self.title