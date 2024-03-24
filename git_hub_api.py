import pprint

import requests

url = 'https://api.github.com/search/code?q=+user:ubi22'
token = ''

session = requests.session()
session.auth = ('vlad132154', token)
result = session.get(url)
pprint.pprint(result.json())
