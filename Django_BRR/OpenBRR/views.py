from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from github.GithubException import RateLimitExceededException
from .models import ModelRepo
from .forms import RepoGithub
from .analize_repo import get_repository, get_language, get_license, get_commits, get_wiki, get_forks, get_subscribers, get_organization

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
            repo = get_repository(request.GET['text'])
            #posts['languages'] = str(get_language(request.GET['text']))
            posts['languages'] = list(repo.get_languages().keys())
            #posts['license'] = get_license((request.GET['text']), request.GET['license'])
            posts['commits'] = repo.get_commits().totalCount
            posts['wiki'] = repo.has_wiki
            posts['forks'] = repo.forks_count
            posts['subscribers'] = repo.subscribers_count
            posts['organization'] = str(get_organization(repo))
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
        except RateLimitExceededException:
            posts['error'] = ('Error: Se ha excedido el número de peticiones a GitHub. Intentelo de nuevo más tarde.')
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
        except Exception:
            posts['error'] = ("Error: " + str(Exception))
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
    else:
        return render(request, 'OpenBRR/main.html', {})