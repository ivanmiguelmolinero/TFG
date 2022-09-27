from ast import If
from github import Github

# Introducimos la token del usuario
g = Github("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")



repo = g.get_repo("github/choosealicense.com")
contents = repo.get_contents("")
for content_file in contents:
    if (content_file.name[:7] == "LICENSE"):
        print("TIENE LICENCIA. CHECK")
        file = content_file.name;
        print("Content name:", content_file.name)