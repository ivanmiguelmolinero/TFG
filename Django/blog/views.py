from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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

# Función que recibe la petición post_new y devuelve la página para añadir un post
def post_new(request):
    if request.method == "POST": # Si hemos rellenado el formulario con un nuevo post y queremos enviarlo
        form = PostForm(request.POST) # Rellenamos el formulario con los datos del POST
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: # Si es la primera vez que entramos
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

# Función que recible la petición post_edit y devuelve o bien la página para editar o bien el post ya editado
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Básicamente el if de la función de arriba
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})