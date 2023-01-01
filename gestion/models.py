from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


# Create your models here.


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)


class Sexo(models.TextChoices):
    MASCULINO = "M", _("masculino")
    FEMENINO = "F", _("femenino")


class Tema(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    fuente = models.CharField(max_length=50)

  

class EstadoPerfil(models.TextChoices):
    APROBADO = "A", _("aprobado")
    DESAPROBADO = "D", _("desaprobado")


class Perfil(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    objeto_estudio = models.CharField(max_length=50)
    objetivo_general = models.CharField(max_length=50)
    contexto_problema = models.CharField(max_length=50)
    estado_perfil = models.CharField(max_length=1, choices=EstadoPerfil.choices)


class Tribunal(models.Model):
    numero = models.IntegerField()


class RolProfesor(models.TextChoices):
    MASCULINO = "M", _("masculino")
    FEMENINO = "F", _("femenino")


class CategotiaDocente(models.TextChoices):
    APROBADO = "A", _("aprobado")
    DESAPROBADO = "D", _("desaprobado")


class Profesor(models.Model):
    user = models.ForeignKey(Usuario, verbose_name=_(""), on_delete=models.CASCADE)
    roles = models.CharField(max_length=1, choices=RolProfesor.choices)
    numero_tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)
    perfil_asociado = models.ForeignKey(Perfil, on_delete=models.CASCADE)


class Estudiante(models.Model):
    user = models.ForeignKey(Usuario, verbose_name=_(""), on_delete=models.CASCADE)
    merito_cientifico = models.IntegerField()


class InformeTesis(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)


class TipoImpacto(models.TextChoices):
    APROBADO = "A", _("aprobado")
    DESAPROBADO = "D", _("desaprobado")


class Sennalamiento(models.Model):
    informe_tesis = models.ForeignKey(InformeTesis, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
