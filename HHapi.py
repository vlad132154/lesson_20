import requests
import pprint
domain = 'https://api.hh.ru/'
url_vacan = f'{domain}vacancies'
params = {
    'text': 'python developer',
    'page': 1
}
result = requests.get(url_vacan, params=params).json()

items = result['items']

first = items[0]
pprint.pprint(first['alternate_url'])

one_vacancy_url = (first['url'])
result1 = requests.get(one_vacancy_url, params=params).json()
pprint.pprint(result1)
