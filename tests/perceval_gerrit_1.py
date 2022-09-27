from datetime import datetime, timedelta
from perceval.backends.core.gerrit import Gerrit

hostname = 'gerrit.opnfv.org'
user = 'user'

from_date = datetime.now() - timedelta(days=1)

repo = Gerrit(hostname=hostname, user=user)

for review in repo.fetch(from_date=from_date):
    print(review['data']['number'])