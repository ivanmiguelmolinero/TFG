from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from github.GithubException import RateLimitExceededException
from .models import ModelRepo
from .forms import RepoGithub
from .analize_repo import get_repository, get_language, get_licencia, get_commits, get_wiki, get_forks, get_subscribers, get_organization

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
        posts_sec = {}
        try:
            # Obtenemos el repositorio introducido por el usuario
            repo = get_repository(request.GET['text'])
            # PESTAÑA DE COMUNIDAD
            posts['languages'] = list(repo.get_languages().keys())
            posts['commits'] = repo.get_commits().totalCount
            posts['wiki'] = repo.has_wiki
            posts['forks'] = repo.forks_count
            posts['subscribers'] = repo.subscribers_count
            posts['organization'] = str(get_organization(repo))
            fecha_update = (str(repo.pushed_at.date().year) + '-' + str(repo.pushed_at.date().month) + '-' + str(repo.pushed_at.date().day))
            posts['lastUpdate'] = repo.pushed_at.date()
            now = datetime.now()
            day = to_valid_format(now.day)
            month = to_valid_format(now.month)
            now = (str(now.year) + '-' + month + '-' + day)

            # PESTAÑA DE SEGURIDAD
            posts_sec['license'] = get_licencia(repo)
            posts_sec['viewers'] = repo.watchers_count

            return render(request, 'OpenBRR/repo_prueba.html', 
                        {'post': posts, 'date': fecha_update, 'now': now,
                        'post_sec': posts_sec})
        except RateLimitExceededException:
            posts['error'] = ('Error: Se ha excedido el número de peticiones a GitHub. Intentelo de nuevo más tarde.')
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
        except Exception:
            posts['error'] = ("Error: " + str(Exception))
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
    else:
        return render(request, 'OpenBRR/main.html', {})

#-- Función que devuelve la fecha en formato correcto
def to_valid_format(date):
    if (date < 10):
        return '0' + str(date)
    else:
        return str(date)