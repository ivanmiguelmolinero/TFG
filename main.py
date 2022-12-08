from github import Github
from github.GithubException import RateLimitExceededException
from datetime import datetime


def to_valid_format(date):
    if (date < 10):
        return '0' + str(date)
    else:
        return str(date)

# Introducimos la token del usuario
print("Key (si no la tiene pulse INTRO):")
key = input()
# Si tenemos la clave también podemos hacer esto
if key != "":
    g = Github(key)
    #Contamos los commits de cada repositorio del usuario
    for repoGit in g.get_user().get_repos():
        print(repoGit.name, repoGit.get_commits().totalCount)
else:
    g = Github()
#repo_path = "PyGithub/PyGithub"
repo_path = "ivanmiguelmolinero/Scappe-Room"

try:
    # Introducimos la dirección del repo
    repo = g.get_repo(repo_path)
    contents = repo.get_contents("") # Obtenemos su contenido
    for content_file in contents: # Comprobamos si alguno es el "LICENSE"
        if (content_file.name[:7] == "LICENSE"):
            print("TIENE LICENCIA. CHECK")
            file = content_file.name
            print("Content name:", content_file.name)


    # Mostramos los commits del repo seleccionado
    print(repo.name)
    print("COMMITS: ", repo.get_commits().totalCount)

    # Mostramos lenguajes utilizados
    print("Lenguaje: ", list(repo.get_languages().keys()))

    #Mostramos la última vez que se actualizó
    fecha = repo.pushed_at
    print("Actualizado por última vez:", repo.pushed_at)

    print("Tiene wiki:", repo.has_wiki)

    print("Forks:", repo.forks_count)

    organizacion = repo.organization
    print("¿Pertenece a una organización?", repo.organization)
    #print("Login: ", organizacion.login)

    has_dld = repo.has_downloads
    downloads = repo.get_downloads()
    print("DESCARGAS: ", has_dld, downloads.totalCount)

    licencia = repo.get_license()

    print("Número de suscriptores: ", repo.subscribers_count)
    fecha_d = str(fecha.date())
    fecha_h = fecha.ctime()
    now = str(datetime.now())
    day = to_valid_format(repo.pushed_at.day)
    month = to_valid_format(repo.pushed_at.month)
    now_day = to_valid_format(datetime.now().day)
    print("p")
    stats = repo.get_stats_code_frequency
    work = repo.get_workflow()
    print(work)
except RateLimitExceededException:
    print("Número máximo de peticiones alcanzadas. Inténtelo de nuevo más tarde.")