from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Log(models.Model):
    details = models.TextField("Detalhes", max_length=500)
    number_events = models.IntegerField("Quantidade de Eventos")
    occurrence_date = models.DateTimeField("Data de Ocorrência", auto_now_add=True)
    title = models.CharField("Título", max_length=100)
    active = models.BooleanField("Ativo", default=True)

    #environment = models.ForeignKey(Environment, on_delete=models.PROTECT, null=True)
    #level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    #origin = models.ForeignKey(Origin, on_delete=models.PROTECT, null=True)
    #user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

class Origin(models.Model):
    description = models.TextField("Descrição", max_length=500)

class User(models.Model):
    name       = models.CharField("Nome", max_length=50)
    email      = models.EmailField("Email", max_length=100)
    password   = models.CharField("Password", max_length=50, validators=[MinLengthValidator(8)])
    last_login = models.DateTimeField("Ultimo Login", auto_now_add=True)

class Environment(models.Model):
    description = models.CharField("Descrição", max_length=50)
