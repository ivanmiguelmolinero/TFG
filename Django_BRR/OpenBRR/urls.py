from django.urls import path
from . import views

urlpatterns = [
    # Para el URL raíz muestro la página principal
    path('', views.post_main, name='post_main'),
    # Para hacer un POST del repo
    path('post', views.post_repo, name='post_repo'),
    # Para enviar los datos del repositorio
    path('get-data', views.get_data, name='get_data')
]