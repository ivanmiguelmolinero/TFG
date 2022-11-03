from django.urls import path
from . import views

urlpatterns = [
    # Para el URL raíz muestro la lista de posts
    path('', views.post_list, name='post_list'),
    # Para el URL de la imagen muestro la imagen
    path('/github.png', views.post_img, name='post_img'),
    # Para el URL post/[entero] devuelvo el post correspondiente a ese entero
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]