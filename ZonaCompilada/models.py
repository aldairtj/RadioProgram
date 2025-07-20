from django.db import models # type: ignore

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='musica_local/')

    def __str__(self):
        return self.titulo

class Oyente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"