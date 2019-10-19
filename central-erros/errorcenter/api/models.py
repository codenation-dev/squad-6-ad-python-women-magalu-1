from django.db import models

# Create your models here.
class Origin(models.Model):
    description = models.TextField("Descrição", max_length=500)