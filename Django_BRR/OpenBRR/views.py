from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from github.GithubException import RateLimitExceededException
from .models import ModelRepo
from .forms import RepoGithub
from .analize_repo import get_repository, get_downloads, get_licencia, get_template, get_projects, get_wiki, get_readme, get_organization

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
        # Inicializo variables de importancia
        issues_count = 0
        posts = {}
        posts_sec = {}
        posts_func = {}
        posts_supp = {}
        posts_qual = {}
        posts_usab = {}
        posts_adop = {}
        try:
            # Obtenemos el repositorio introducido por el usuario
            repo = get_repository(request.GET['text'])
            # PESTAÑA DE COMUNIDAD
            posts['commits'] = repo.get_commits().totalCount
            posts['forks'] = repo.forks_count
            posts['subscribers'] = repo.subscribers_count
            posts['organization'] = str(get_organization(repo))
            fecha_update = (str(repo.pushed_at.year) + '-' + 
                            to_valid_format(repo.pushed_at.month) + '-' +
                            to_valid_format(repo.pushed_at.day))
            posts['lastUpdate'] = fecha_update
            now = datetime.now()
            day = to_valid_format(now.day)
            month = to_valid_format(now.month)
            now = (str(now.year) + '-' + month + '-' + day)

            # PESTAÑA DE SEGURIDAD
            posts_sec['license'] = get_licencia(repo)
            posts_sec['viewers'] = repo.watchers_count
            posts_sec['vulnerability'] = repo.get_vulnerability_alert
            if repo.open_issues_count != 0: #-- Si el repo tiene problemas abiertos, obtengo su cantidad
                posts_sec['issues'] = 'Sí'
                issues_count = repo.open_issues_count
            else:
                posts_sec['issues'] = 'No'

            
            # PESTAÑA DE FUNCIONALIDAD
            posts_func['size'] = repo.size
            posts_func['template'] = get_template(repo)
            posts_func['projects'] = get_projects(repo)

            # PESTAÑA DE SOPORTE
            posts_supp['wiki'] = get_wiki(repo)
            posts_supp['homepage'] = str(repo.homepage)

            # PESTAÑA DE CALIDAD
            posts_qual['followers_owner'] = repo.owner.followers
            posts_qual['n_repos'] = repo.owner.public_repos
            if posts['organization'] != 'None': #-- Si pertenece a una organización, sacamos sus datos
                posts_qual['followers_org'] = str(repo.organization.followers)
                posts_qual['n_repos_org'] = repo.organization.public_repos
            else: #-- Si no, ponemos sus contadores a 0
                posts_qual['followers_org'] = '0'
                posts_qual['n_repos_org'] = '0'

            # PESTAÑA DE USABILIDAD
            posts_usab['num_languages'] = len(list(repo.get_languages().keys()))
            posts_usab['readme'] = get_readme(repo)

            # PESTAÑA DE ADOPCIÓN
            posts_adop['downloads'] = get_downloads(repo)
            return render(request, 'OpenBRR/repo_prueba.html', 
                        {'post': posts, 'date': fecha_update, 'now': now,
                        'post_sec': posts_sec, 'issues': issues_count,
                        'post_func': posts_func,
                        'post_supp': posts_supp,
                        'post_qual': posts_qual,
                        'post_usab': posts_usab,
                        'post_adop': posts_adop})
        except RateLimitExceededException:
            posts['error'] = ('Error: Se ha excedido el número de peticiones a GitHub. Intentelo de nuevo más tarde.')
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts})
        except Exception:
            posts['error'] = ("Error: " + str(Exception.args))
            return render(request, 'OpenBRR/repo_prueba.html', {'post': posts, 'now': now,
                        'post_sec': posts_sec, 'issues': issues_count,
                        'post_func': posts_func,
                        'post_supp': posts_supp,
                        'post_qual': posts_qual,
                        'post_usab': posts_usab,
                        'post_adop': posts_adop})
    else:
        return render(request, 'OpenBRR/main.html', {})

def get_data(request):
    if request.method == 'GET':
        commits = int(request.GET['commits'])
        valor_commits = float(request.GET['valor-commits'])
        nota_commits = calc_nota_commits(commits) 
        nota_commits_pond = nota_commits * (valor_commits/100) #-- Nota ponderada con su peso
        forks = int(request.GET['forks'])
        valor_forks = float(request.GET['valor-forks'])
        nota_forks = calc_nota_forks(forks) 
        nota_forks_pond = nota_forks * (valor_forks/100) #-- Nota ponderada con su peso
        suscriptores = int(request.GET['suscriptores'])
        valor_suscriptores = float(request.GET['valor-suscriptores'])
        nota_sus = calc_nota_sus(suscriptores)
        nota_sus_pond = nota_sus * (valor_suscriptores/100) #-- Nota ponderada con su peso
        organization = request.GET['organization']
        valor_organizacion = float(request.GET['valor-organización'])
        nota_org = calc_nota_org(organization)
        nota_org_pond = nota_org * (valor_organizacion/100) #-- Nota ponderada con su peso
        update = request.GET['update']
        valor_update = float(request.GET['valor-actualización'])
        nota_upd = calc_nota_update(update)
        nota_upd_pond = nota_upd * (valor_update/100) #-- Nota ponderada con su peso
        nota_comunidad = nota_commits_pond + nota_forks_pond + nota_sus_pond + nota_org_pond + nota_upd_pond
        return render(request, 'OpenBRR/result.html', {'nota_commits': nota_commits,
                                                        'nota_forks': nota_forks,
                                                        'nota_suscriptores': nota_sus,
                                                        'nota_org': nota_org,
                                                        'nota_update': nota_upd,
                                                        'nota_comunidad': nota_comunidad})

def calc_nota_commits(com):
    # Calculamos la nota de los commits
    if (com > 20) or (com <= 20):
        nota_commits = 2.5
    elif (com > 20) or (com <= 60):
        nota_commits = 5
    elif (com > 60) or (com <= 100):
        nota_commits = 7.5
    elif com > 100:
        nota_commits = 10
    else:
        nota_commits = 0
    return nota_commits #-- Nota ponderada con su peso

def calc_nota_forks(forks):
    # Calculamos la nota de los forks
    if (forks > 0) or (forks <= 50):
        nota_forks = 2.5
    elif (forks > 500) or (forks <= 150):
        nota_forks = 5
    elif (forks > 160) or (forks <= 500):
        nota_forks = 7.5
    elif forks > 500:
        nota_forks = 10
    else:
        nota_forks = 0
    return nota_forks

def calc_nota_sus(sus):
    # Calculamos la nota de las suscripciones
    if (sus > 20) or (sus <= 20):
        nota_sus = 2.5
    elif (sus > 20) or (sus <= 60):
        nota_sus = 5
    elif (sus > 60) or (sus <= 100):
        nota_sus = 7.5
    elif sus > 100:
        nota_sus = 10
    else:
        nota_sus = 0
    return nota_sus

def calc_nota_org(org):
    # Calculamos la nota de pertenecer o no a una organización
    if org == 'Sí':
        nota_org = 10
    elif org == 'No':
        nota_org = 0
    return nota_org

def calc_nota_update(upd):
    # Calculamos la nota de la actualización
    now = datetime.now()
    day = to_valid_format(now.day)
    month = to_valid_format(now.month)
    year = str(now.year)
    # Separamos el día, el mes y el año de la última actualización
    upd_separado = upd.split('-')
    if year == upd_separado[0]:
        if month == upd_separado[1]:
            if day == upd_separado[2]:
                nota_upd = 10 # Se ha actualizado hoy
            else:
                nota_upd = 7.5 # Se ha actualizado este mes
        else:
            nota_upd = 5 # Se ha actualizado este año
    else:
        nota_upd = 2.5 # No se ha actualizado este año
    return nota_upd

def calc_nota_comunidad(com, v_com, forks, v_forks, sus, v_sus, org, v_org, upd, v_upd):
    pass


#-- Función que devuelve la fecha en formato correcto
def to_valid_format(date):
    if (date < 10):
        return '0' + str(date)
    else:
        return str(date)