from django.db import models

# Create your models here.
class ModelRepo(models.Model):
    repo_name = models.TextField()

     #-- Publica una nueva entrada en el blog
    def publish(self):
        self.save()

    #-- Devuelve el nombre del repositorio
    def __str__(self):
        return self.repo_name