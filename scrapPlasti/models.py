from django.db import models
from base.models import Producto


# Create your models here.
class TablaScrap(models.Model):
    Producto_base = models.ForeignKey(Producto, on_delete=models.CASCADE)
    url_Scrap = models.URLField()
    frec_Scrap= models.PositiveIntegerField()
    codigo_interno = models.CharField(max_length=50)

    def __str__(self):
        return f'Scraping de {self.Producto_base.nombre}'