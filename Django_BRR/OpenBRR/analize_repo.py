from github import Github

# # Introducimos la token del usuario
# print("Key (si no la tiene pulse INTRO):")
# key = input()
# # Si tenemos la clave también podemos hacer esto
# if key != "":
#     g = Github(key)
#     #Contamos los commits de cada repositorio del usuario
#     for repoGit in g.get_user().get_repos():
#         print(repoGit.name, repoGit.get_commits().totalCount)
# else:
#     g = Github()
# #repo_path = "PyGithub/PyGithub"
# repo_path = "ivanmiguelmolinero/Scappe-Room"

# # Introducimos la dirección del repo
# repo = g.get_repo(repo_path)
# contents = repo.get_contents("") # Obtenemos su contenido
# for content_file in contents: # Comprobamos si alguno es el "LICENSE"
#     if (content_file.name[:7] == "LICENSE"):
#         print("TIENE LICENCIA. CHECK")
#         file = content_file.name
#         print("Content name:", content_file.name)


# # Mostramos los commits del repo seleccionado
# print(repo.name)
# print("COMMITS: ", repo.get_commits().totalCount)

# # Mostramos lenguajes utilizados
# print("Lenguaje: ", list(repo.get_languages().keys()))

# #Mostramos la última vez que se actualizó
# print("Actualizado por última vez:", repo.updated_at)

#-- Obtiene los lenguajes del repositorio
def get_language(data):
    g = Github()
    repo_path = data
    repo = g.get_repo(repo_path)
    return list(repo.get_languages().keys())

#-- Comprueba si tiene un archivo de licencia
def get_license(repo_data, data):
    if data == '':
        g = Github()
        repo_path = repo_data
        repo = g.get_repo(repo_path)
        contents = repo.get_contents("") # Obtenemos su contenido
        license_found = False
        for content_file in contents: # Comprobamos si alguno es el "LICENSE"
            if (content_file.name[:7] == "LICENSE"):
                return 'Sí'
        if not license_found:
            return 'No'
    else:
        return data