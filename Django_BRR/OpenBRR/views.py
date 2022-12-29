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

        # Valoración de la pestaña comunidad
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
        nota_comunidad = round(nota_commits_pond + nota_forks_pond + nota_sus_pond + nota_org_pond + nota_upd_pond, 2)

        # Valoración de la pestaña seguridad
        licencia = request.GET['license']
        valor_licencia = float(request.GET['valor-licencia'])
        nota_licencia = calc_nota_licencia(licencia)
        nota_licencia_pond = nota_licencia * (valor_licencia/100)
        viewers = int(request.GET['viewers'])
        valor_viewers = float(request.GET['valor-viewers'])
        nota_viewers = calc_nota_viewers(viewers)
        nota_viewers_pond = nota_viewers * (valor_viewers/100)
        issues = request.GET['issues']
        if issues == 'Sí': #Si hay problemas obtenemos su número
            n_issues = int(request.GET['n_problemas'])
        else: # Si no lo dejamos a 0
            n_issues = 0
        valor_problemas = float(request.GET['valor-problemas'])
        nota_problemas = calc_nota_problemas(issues, n_issues)
        nota_problemas_pond = nota_problemas * (valor_problemas/100)
        vulnerabilidad = request.GET['vulnerability']
        valor_vulnerabilidad = float(request.GET['valor-vulnerabilidad'])
        nota_vulnerabilidad = calc_nota_vulnerabilidad(vulnerabilidad)
        nota_vulnerabilidad_pond = nota_vulnerabilidad * (valor_vulnerabilidad/100)
        nota_seguridad = round(nota_licencia_pond + nota_viewers_pond + nota_problemas_pond + nota_vulnerabilidad_pond, 2)

        # Valoración de la pestaña funcionalidad
        tamaño = int(request.GET['size'])
        valor_tamaño = float(request.GET['valor-tamaño'])
        nota_tamaño = calc_nota_tamaño(tamaño)
        nota_tamaño_pond = nota_tamaño * (valor_tamaño/100)
        plantilla = request.GET['template']
        valor_plantilla = float(request.GET['valor-plantilla'])
        nota_plantilla = calc_nota_plantilla(plantilla)
        nota_plantilla_pond = nota_plantilla * (valor_plantilla/100)
        proyectos = request.GET['projects']
        valor_proyectos = float(request.GET['valor-proyectos'])
        nota_proyectos = calc_nota_plantilla(proyectos)
        nota_proyectos_pond = nota_proyectos * (valor_proyectos/100)
        nota_funcionalidad = round(nota_tamaño_pond + nota_plantilla_pond + nota_proyectos_pond, 2)
        return render(request, 'OpenBRR/result.html', {'nota_commits': nota_commits,
                                                        'nota_forks': nota_forks,
                                                        'nota_suscriptores': nota_sus,
                                                        'nota_org': nota_org,
                                                        'nota_update': nota_upd,
                                                        'nota_comunidad': nota_comunidad,
                                                        'nota_licencia': nota_licencia,
                                                        'nota_viewers': nota_viewers,
                                                        'nota_problemas': nota_problemas,
                                                        'nota_vulnerabilidad': nota_vulnerabilidad,
                                                        'nota_seguridad': nota_seguridad,
                                                        'nota_tamaño': nota_tamaño,
                                                        'nota_plantilla': nota_plantilla,
                                                        'nota_proyectos': nota_proyectos,
                                                        'nota_funcionalidad': nota_funcionalidad})

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
    if (forks > 0) and (forks <= 50):
        nota_forks = 2.5
    elif (forks > 500) and (forks <= 150):
        nota_forks = 5
    elif (forks > 160) and (forks <= 500):
        nota_forks = 7.5
    elif forks > 500:
        nota_forks = 10
    else:
        nota_forks = 0
    return nota_forks

def calc_nota_sus(sus):
    # Calculamos la nota de las suscripciones
    if (sus > 5) and (sus <= 20):
        nota_sus = 2.5
    elif (sus > 20) and (sus <= 60):
        nota_sus = 5
    elif (sus > 60) and (sus <= 100):
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

def calc_nota_licencia(licencia):
    # Calculamos la nota de la licencia
    if licencia == 'Sí':
        nota_licencia = 10
    else:
        nota_licencia = 0
    return nota_licencia

def calc_nota_viewers(vw):
    # Calculamos la nota de los viewers
    if (vw > 200) and (vw <= 500):
        nota_vw = 2.5
    elif (vw > 500) and (vw <= 800):
        nota_vw = 5
    elif (vw > 800) and (vw <= 1200):
        nota_vw = 7.5
    elif vw > 1200:
        nota_vw = 10
    else:
        nota_vw = 0
    return nota_vw

def calc_nota_problemas(issues ,problemas):
    # Calculamos la nota de los problemas
    if issues == 'Sí':
        if (problemas > 50) and (problemas <= 100):
            nota_problemas = 7.5
        elif (problemas > 100) and (problemas <= 250):
            nota_problemas = 5
        elif (problemas > 250) and (problemas <= 500):
            nota_problemas = 2.5
        elif problemas > 500:
            nota_problemas = 0
        else:
            nota_problemas = 10
    else:
        nota_problemas = 10
    return nota_problemas

def calc_nota_vulnerabilidad(vulnerabilidad):
    # Calculamos la nota de la vulnerabilidad
    if vulnerabilidad == 'Sí':
        nota_vulnerabilidad = 0
    else:
        nota_vulnerabilidad = 10
    return nota_vulnerabilidad

def calc_nota_tamaño(size):
    # Calculamos la nota del tamaño
    if (size > 1000) and (size <= 5000):
        nota_tamaño = 7.5
    elif (size > 5000) and (size <= 10000):
        nota_tamaño = 5
    elif (size > 10000) and (size <= 15000):
        nota_tamaño = 2.5
    elif size > 15000:
        nota_tamaño = 0
    else:
        nota_tamaño = 10
    return nota_tamaño

def calc_nota_plantilla(plantilla):
    # Calculamos la nota de la plantilla
    if plantilla == 'Sí':
        nota_plantilla = 10
    else:
        nota_plantilla  = 0
    return nota_plantilla

def calc_nota_proyectos(proyectos):
    # Calculamos la nota de los proyectos
    if proyectos == 'Sí':
        nota_proyectos = 10
    else:
        nota_proyectos  = 0
    return nota_proyectos

#-- Función que devuelve la fecha en formato correcto
def to_valid_format(date):
    if (date < 10):
        return '0' + str(date)
    else:
        return str(date)