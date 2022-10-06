from github import Github

# Introducimos la token del usuario
print("Key:")
key = input()
g = Github(key)
repo_path = "ivanmiguelmolinero/Scappe-Room"

# Introducimos la dirección del repo
repo = g.get_repo(repo_path)
contents = repo.get_contents("") # Obtenemos su contenido
for content_file in contents: # Comprobamos si alguno es el "LICENSE"
    if (content_file.name[:7] == "LICENSE"):
        print("TIENE LICENCIA. CHECK")
        file = content_file.name
        print("Content name:", content_file.name)

# Contamos los commits
for repoGit in g.get_user().get_repos():
    print(repoGit.name, repoGit.get_commits().totalCount)

# Mostramos los commits del repo seleccionado
print(repo.name)
print("COMMITS: ", repo.get_commits().totalCount)

# Mostramos lenguajes utilizados
print("Lenguaje: ", list(repo.get_languages().keys()))