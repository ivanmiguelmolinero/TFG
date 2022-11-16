from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ModelRepo
from .forms import RepoGithub
from .analize_repo import get_language, get_license

# Create your views here.

# Función que recibe la petición post_main y devuelve un HTML
def post_main(request):
    if request.method == 'POST':
        post = get_object_or_404(ModelRepo)
        return render(request, 'OpenBRR/repo_prueba.html', {'post': post})
    else:
        form = RepoGithub()
        return render(request, 'OpenBRR/main.html', {'form': form})

def post_repo(request):
    if request.method == 'GET':
        posts = []
        posts.append('Este repo usa los siguientes lenguajes: ' + str(get_language(request.GET['text'])))
        posts.append('Licencia: ' + get_license((request.GET['text']), request.GET['license']))
        #posts = ('Este repo usa los siguientes lenguajes:', get_language(request.GET['text']),
         #        '<br> Licencia: ', get_license(request.GET['license']))
        return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
    else:
        return render(request, 'OpenBRR/main.html', {})