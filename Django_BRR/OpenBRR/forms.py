from django import forms
from .models import ModelRepo

#-- Formulario para rellenar con el nombre del repositorio a analizar
class RepoGithub(forms.Form):
    
    class Meta:
        model = ModelRepo
        fields = ('text')