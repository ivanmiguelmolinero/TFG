from django.urls import path
from . import views

urlpatterns = [
    # Para el URL raíz muestro la página principal
    path('', views.post_main, name='post_main'),
    # Para hacer un POST del repo
    path('post', views.post_repo, name='post_repo')
#     # Para el URL de la imagen muestro la imagen
#     path('/github.png', views.post_img, name='post_img'),
#     # Para el URL post/[entero] devuelvo el post correspondiente a ese entero
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     # Para la petición de nuevo post devolvemos la view_post
#     path('post/new', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
]