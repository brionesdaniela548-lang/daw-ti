from django.db import models


# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    titulo = models.CharField(max_length=100, verbose_name='Titulo Academico')
    biografia = models.CharField(max_length=100, verbose_name='Biografia')
    email = models.EmailField(max_length=100, verbose_name='Email')
    trabajo = models.CharField(max_length=100, verbose_name='Ocupacion')
    create = models.DateTimeField(verbose_name='fecha de Creacion', auto_now_add=True)
    update = models.DateTimeField(verbose_name='Fecha de edicion', auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        ordering = ['-create']
        db_table = 'Persona'

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    image = models.ImageField(upload_to="projects/", null=True, blank=True)

    def __str__(self):
        return self.title
