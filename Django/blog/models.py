from django.conf import settings
from django.db import models
from django.utils import timezone

#-- Objeto de publicación el blog con sus partes correspondientes
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank= True, null = True)
    
    #-- Publica una nueva entrada en el blog
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    #-- Devuelve el título de la publicación
    def __str__(self):
        return self.title