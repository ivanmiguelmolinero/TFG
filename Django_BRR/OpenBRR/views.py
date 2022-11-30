from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ModelRepo
from .forms import RepoGithub
from .analize_repo import get_language, get_license, get_commits, get_wiki

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
        posts = {}
        try:
            # posts.append(str(get_language(request.GET['text'])))
            # posts.append( get_license((request.GET['text']), request.GET['license']))
            # posts.append(get_commits(request.GET['text'], request.GET['commits']))
            # posts.append(get_wiki(request.GET['text']))
            posts['languages'] = str(get_language(request.GET['text']))
            posts['license'] = get_license((request.GET['text']), request.GET['license'])
            posts['commits'] = get_commits(request.GET['text'], request.GET['commits'])
            posts['wiki'] = get_wiki(request.GET['text'])
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
        except:
            posts['eror'] = ('Error 404: Es posible que el nombre del repositorio esté mal o ' +
                            'que se haya excedido el número de peticiones a Github.')
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
    else:
        return render(request, 'OpenBRR/main.html', {})