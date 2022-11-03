from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

# Función que recibe la petición post_list y devuelve un HTML
def post_list(request):
    # Posts ordenados de forma inversa a su momento de publicación
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

# Función que recibe la petición post_img y devuelve la imagen
def post_img(request):
    return render(request, 'blog/github.png', {'Content-type:' 'image/png'})

# Función que recibe la petición post_detail y devuelve el post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})