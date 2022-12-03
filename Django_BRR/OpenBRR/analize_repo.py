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
def get_license(repo_data, data):
    if data == '': #-- Si el usuario no ha introducido nada manualmente, lo analizamos
        repo_path = repo_data
        repo = g.get_repo(repo_path)
        contents = repo.get_contents("") # Obtenemos su contenido
        license_found = False
        for content_file in contents: # Comprobamos si alguno es el "LICENSE"
            if (content_file.name[:7] == "LICENSE"):
                return 'Sí'
        if not license_found:
            return 'No'
    else: #-- Si no devolvemos lo que ha introducido
        return data
    
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