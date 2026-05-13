from django.db import models


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to= 'portfolio' , null=True, blank=True)
    create = models.DateTimeField(verbose_name='fecha de Creacion' ,auto_now_add=True)
    update = models.DateTimeField(verbose_name='Fecha de edicion', auto_now=True) #se va a editar la ultima fecha que yo edite, funciona como auditoria
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'portafolio'
        verbose_name_plural = 'portafolios'
        ordering = ['-create']
        db_table = 'portfolio' #esta clase ayuda a personalizar los datos

class Tarea(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    archivo = models.FileField(upload_to= 'portfolio/')

objects = models.Manager()
