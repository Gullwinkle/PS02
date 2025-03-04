import requests
from pprint import pprint


url = 'https://api.github.com/search/repositories'
url2 = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'q': 'html',
}
response = requests.get(url, params=params)
print(response.status_code)
pprint(response.json())

params2 = {
    'userId': 1
}
response = requests.get(url2, params=params2)
print(response.status_code)
pprint(response.json())

data = {
    'title': 'тестовый post запрос',
    'body': 'тестовый контент post запроса',
    'userId': 2
}
response = requests.post(url2, data=data)
print(response.status_code)
pprint(response.json())