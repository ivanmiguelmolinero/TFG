from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ModelRepo
from .forms import RepoGithub

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
        posts = request.GET['text']
        return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
    else:
        return render(request, 'OpenBRR/main.html', {})