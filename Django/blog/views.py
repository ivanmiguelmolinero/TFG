from email.mime import image
from django.shortcuts import render

# Create your views here.

# Función que recibe la petición post_list y devuelve un HTML
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Función que recibe la petición post_img y devuelve la imagen
def post_img(request):
    return render(request, 'blog/github.png', content_type='image/png')