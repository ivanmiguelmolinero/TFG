import argparse
from ast import arg
from perceval.backends.core.github import GitHub

# Parse command line arguments
parser = argparse.ArgumentParser(
    description= "Simple parser for Github issues and pull requests"
)
parser.add_argument("-t", "--token",
                    '--nargs', nargs='+',
                    help= "Github token")
parser.add_argument("-r", "--repo",
                    help= "Github repository, as 'owner/repo'")
args = parser.parse_args()

# Owner and repository names
(owner, repo) = args.repo.split('/')

# Create a Git object, pointig to repo_url, using repo_dir for cloning
repo = GitHub(owner=owner, repository=repo, api_token=args.token)
# Fetch all issues/pull requests as an iterator, and iterate it printing
# their number, and wether they are issues or pull requests
for item in repo.fetch():
    if 'pull_request' in item['data']:
        kind = 'Pull request'
    else:
        kind = 'Issue'
    print(item['data']['number'], ':', kind)