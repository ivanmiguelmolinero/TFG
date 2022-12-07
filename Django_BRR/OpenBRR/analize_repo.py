from github import Github

g = Github()

#-- Función que obtiene el repositorio a partir de su path
def get_repository(data):
    repo_path = data
    return g.get_repo(repo_path)

#-- Obtiene los lenguajes del repositorio
def get_language(data):
    repo_path = data
    repo = g.get_repo(repo_path)
    return list(repo.get_languages().keys())

#-- Comprueba si tiene un archivo de licencia
def get_licencia(repo):
    try:
        repo.get_license()
        return 'Sí'
    except:
        return 'No'
    
def get_commits(data, num_commits):
    if num_commits == '': #-- Si el usuario no ha introducido nada manualmente, lo analizamos
        repo_path = data
        repo = g.get_repo(repo_path)
        return str(repo.get_commits().totalCount)
    else: #-- Si no devolvemos lo que ha introducido
        return num_commits

def get_wiki(data):
    repo_path = data
    repo = g.get_repo(repo_path)
    return repo.has_wiki

def get_forks(data):
    repo = get_repository(data)
    return repo.forks_count

def get_organization(repo):
    if str(repo.organization) == 'None':
        return repo.organization
    else:
        return repo.organization.login

def get_subscribers(data):
    repo = get_repository(data)
    return repo.subscribers_count