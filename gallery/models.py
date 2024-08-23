from datetime import datetime
from django.db import models

class Fotografia(models.Model):

  CATEGORY_OPTIONS = [
    ("NEBULOSA", "Nebulosa"),
    ("ESTRELA", "Estrela"),
    ("GALÁXIA", "Galáxia"),
    ("PLANETA", "Planeta")
  ]

  name = models.CharField(max_length=100, null=False, blank=False)
  subtitle = models.CharField(max_length=150, null=False, blank=False)
  category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
  description = models.TextField(null=False,blank=False)
  foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
  public= models.BooleanField(default=False)
  data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

  def __str__(self):
    return self.name