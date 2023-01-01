from django.forms import ModelForm
from .models import Tema
from django import forms


class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = ["titulo", "descripcion", "fuente"]

