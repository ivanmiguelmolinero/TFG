from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime
from github.GithubException import RateLimitExceededException
from .models import ModelRepo
from .forms import RepoGithub
from .analize_repo import get_repository, get_downloads, get_licencia, get_template, get_projects, get_wiki, get_readme, get_organization

# Create your views here.

# Función que recibe la petición post_main y devuelve un HTML
def post_main(request):
    if request.method == 'POST':
        try:
            post = get_object_or_404(ModelRepo)
            return render(request, 'OpenBRR/repo_data.html', {'post': post})
        except:
            return render(request, 'OpenBRR/error.html', {})
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
            return render(request, 'OpenBRR/repo_data.html', 
                        {'post': posts, 'date': fecha_update, 'now': now,
                        'post_sec': posts_sec, 'issues': issues_count,
                        'post_func': posts_func,
                        'post_supp': posts_supp,
                        'post_qual': posts_qual,
                        'post_usab': posts_usab,
                        'post_adop': posts_adop})
        except RateLimitExceededException:
            return render(request, 'OpenBRR/overflow.html', {})
        except Exception:
            return render(request, 'OpenBRR/error.html', {})
    else:
        return render(request, 'OpenBRR/main.html', {})

def get_data(request):
    #Lista para enviar los resultados
    user_dest = []

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
        nota_comunidad = round((nota_commits_pond + nota_forks_pond + nota_sus_pond + nota_org_pond + nota_upd_pond)/2, 2)

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
        nota_seguridad = round((nota_licencia_pond + nota_viewers_pond + nota_problemas_pond + nota_vulnerabilidad_pond)/2, 2)

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
        nota_funcionalidad = round((nota_tamaño_pond + nota_plantilla_pond + nota_proyectos_pond)/2, 2)

        # Valoración de la pestaña de soporte
        wiki = request.GET['wiki']
        valor_wiki = float(request.GET['valor-wiki'])
        nota_wiki = calc_nota_wiki(wiki)
        nota_wiki_pond = nota_wiki * (valor_wiki/100)
        homepage = request.GET['homepage']
        valor_homepage = float(request.GET['valor-homepage'])
        nota_homepage = calc_nota_homepage(homepage)
        nota_homepage_pond = nota_homepage * (valor_homepage/100)
        nota_soporte = round((nota_wiki_pond + nota_homepage_pond)/2, 2)

        # Valoración de la pestaña de calidad
        seguidores_own = int(request.GET['followers_owner'])
        valor_seguidores_own = float(request.GET['valor-seg-dueño'])
        nota_seguidores_own = calc_nota_seguidores(seguidores_own)
        nota_seguidores_own_pond = nota_seguidores_own * (valor_seguidores_own/100)
        repositorios_own = int(request.GET['n_repos'])
        valor_repositorios_own = float(request.GET['valor-repos-dueño'])
        nota_repositorios_own = calc_nota_repos(repositorios_own)
        nota_repositorios_own_pond = nota_repositorios_own * (valor_repositorios_own/100)
        seguidores_org = int(request.GET['followers_org'])
        valor_seguidores_org = float(request.GET['valor-seg-org'])
        nota_seguidores_org = calc_nota_seguidores(seguidores_org)
        nota_seguidores_org_pond = nota_seguidores_org * (valor_seguidores_org/100)
        repositorios_org = int(request.GET['n_repos_org'])
        valor_repositorios_org = float(request.GET['valor-repos-org'])
        nota_repositorios_org = calc_nota_repos(repositorios_org)
        nota_repositorios_org_pond = nota_repositorios_org * (valor_repositorios_org/100)
        nota_calidad = round((nota_seguidores_own_pond + nota_repositorios_own_pond + nota_repositorios_org_pond + nota_seguidores_org_pond)/2, 2)

        # Valoración de la pestaña de usabilidad
        num_lenguajes = int(request.GET['num-languages'])
        valor_num_lenguajes = float(request.GET['valor-lenguajes'])
        nota_num_lenguajes = calc_nota_num_lenguajes(num_lenguajes)
        nota_num_lenguajes_pond = nota_num_lenguajes * (valor_num_lenguajes/100)
        readme = request.GET['readme']
        valor_readme = float(request.GET['valor-readme'])
        nota_readme = calc_nota_readme(readme)
        nota_readme_pond = nota_readme * (valor_readme/100)
        nota_usabilidad = round((nota_num_lenguajes_pond + nota_readme_pond)/2, 2)

        # Valoración de la pestaña de adopción
        descargas = request.GET['downloads']
        valor_descargas = float(request.GET['valor-descargas'])
        nota_descargas = calc_nota_descargas(descargas)
        nota_descargas_pond = nota_descargas * (valor_descargas/100)
        nota_adopcion = round(nota_descargas_pond/2, 2)

        # Cálculo de la nota final del repositorio sobre 5
        nota_final = round(((nota_comunidad + nota_seguridad + nota_funcionalidad + nota_soporte + nota_calidad + nota_usabilidad + nota_adopcion)/7)*0.5, 2)

        # Formamos el mensaje y lo enviamos
        mensaje = ('COMUNIDAD\n' + 'Nota de los commits: ' + str(nota_commits) +
                    '\nNota de los forks: ' + str(nota_forks) +
                    '\nNota de los suscriptores: ' + str(nota_sus) +
                    '\nNota de la organización: ' + str(nota_org) +
                    '\nNota update: ' + str(nota_upd) +
                    '\nNOTA FINAL DE LA COMUNIDAD: ' + str(nota_comunidad) +
                    '\n\nSEGURIDAD\n' +  'Nota de la licencia: ' + str(nota_licencia) +
                    '\nNota de los viewers: ' + str(nota_viewers) +
                    '\nNota de los problemas: ' + str(nota_problemas) +
                    '\nNota de la vulnerabilidad: ' + str(nota_vulnerabilidad) +
                    '\nNOTA FINAL DE LA SEGURIDAD: ' + str(nota_seguridad) +
                    '\n\nFUNCIONALIDAD\n' + 'Nota del tamaño: ' + str(nota_tamaño) +
                    '\nNota de la plantilla: ' + str(nota_plantilla) +
                    '\nNota de los proyectos: ' + str(nota_proyectos) +
                    '\nNOTA FINAL DE LA FUNCIONALIDAD: ' + str(nota_funcionalidad) +
                    '\n\nSOPORTE\n' + 'Nota de la wiki: ' + str(nota_wiki) +
                    '\nNota de la homepage: ' + str(nota_homepage) +
                    '\nNOTA FINAL DE SOPORTE: ' + str(nota_soporte) + 
                    '\n\nCALIDAD\n' + 'Nota de los seguidores del dueño: ' + str(nota_seguidores_own) +
                    '\nNota de los repositorios del dueño: ' + str(nota_repositorios_own) +
                    '\nNota de los seguidores de la organización: ' + str(nota_seguidores_org) +
                    '\nNota de los repositorios de la organización: ' + str(nota_repositorios_org) +
                    '\nNOTA FINAL DE CALIDAD: ' + str(nota_calidad) +
                    '\n\nUSABILIDAD\n' + 'Nota del número de lenguajes: ' + str(nota_num_lenguajes) +
                    '\nNota del README: ' + str(nota_readme) +
                    '\nNOTA FINAL DE USABILIDAD: ' + str(nota_usabilidad) +
                    '\n\nADOPCIÓN\n' + 'Nota de las descargas: ' + str(nota_descargas) +
                    '\nNOTA FINAL DE ADOPCIÓN: ' + str(nota_adopcion) +
                    '\n\nNOTA FINAL DEL REPOSITORIO: ' + str(nota_final))
        user_dest.append(request.GET['email'])
        try:
            send_mail(
                'Resultado de los análisis del repositorio', # Asunto
                mensaje, # Cuerpo del mensaje
                'i.miguel.molinero@gmail.com', # Usuario que envía el email
                user_dest, # Usuario al que se envía el email
                fail_silently=False,
            )
        except:
            pass
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
                                                        'nota_funcionalidad': nota_funcionalidad,
                                                        'nota_wiki': nota_wiki,
                                                        'nota_homepage': nota_homepage,
                                                        'nota_soporte': nota_soporte,
                                                        'nota_seguidores_own': nota_seguidores_own,
                                                        'nota_repositorios_own': nota_repositorios_own,
                                                        'nota_seguidores_org': nota_seguidores_org,
                                                        'nota_repositorios_org': nota_repositorios_org,
                                                        'nota_calidad': nota_calidad,
                                                        'nota_num_lenguajes': nota_num_lenguajes,
                                                        'nota_readme': nota_readme,
                                                        'nota_usabilidad': nota_usabilidad,
                                                        'nota_descargas': nota_descargas,
                                                        'nota_adopcion': nota_adopcion,
                                                        'nota_final': nota_final})

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

def calc_nota_wiki(wiki):
    # Calculamos la nota de la wiki
    if wiki == 'Sí':
        nota_wiki = 10
    else:
        nota_wiki  = 0
    return nota_wiki

def calc_nota_homepage(homepage):
    # Calculamos la nota de la hompeage
    if homepage == 'Sí':
        nota_homepage = 10
    else:
        nota_homepage  = 0
    return nota_homepage

def calc_nota_seguidores(seguidores):
    # Calculamos la nota de los seguidores del dueño y de la organización
    if (seguidores > 50) and (seguidores <= 250):
        nota_seguidores = 2.5
    elif (seguidores > 250) and (seguidores <= 750):
        nota_seguidores = 5
    elif (seguidores > 750) and (seguidores <= 1250):
        nota_seguidores = 2.5
    elif seguidores > 1250:
        nota_seguidores = 10
    else:
        nota_seguidores = 0
    return nota_seguidores

def calc_nota_repos(repos):
    # Calculamos la nota de los repositorios del dueño y de la organización
    if (repos > 5) and (repos <= 15):
        nota_repos = 2.5
    elif (repos > 15) and (repos <= 30):
        nota_repos = 5
    elif (repos > 30) and (repos <= 50):
        nota_repos = 2.5
    elif repos > 50:
        nota_repos = 10
    else:
        nota_repos = 0
    return nota_repos

def calc_nota_num_lenguajes(num):
    # Calculamos la nota del número de lenguajes utilizados en el repositorio
    if (num > 3) and (num <= 6):
        nota_lenguajes = 7.5
    elif (num > 6) and (num <= 8):
        nota_lenguajes = 5
    elif (num > 8) and (num <= 12):
        nota_lenguajes = 2.5
    elif num > 12:
        nota_lenguajes = 0
    else:
        nota_lenguajes = 10
    return nota_lenguajes

def calc_nota_readme(readme):
    # Calculamos la nota del readme
    if readme == 'Sí':
        nota_readme = 10
    else:
        nota_readme  = 0
    return nota_readme

def calc_nota_descargas(descargas):
    # Calculamos la nota de las descargas
    if descargas == 'Sí':
        nota_descargas = 10
    else:
        nota_descargas  = 0
    return nota_descargas

#-- Función que devuelve la fecha en formato correcto
def to_valid_format(date):
    if (date < 10):
        return '0' + str(date)
    else:
        return str(date)