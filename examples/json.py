import requests
import json

def space(need):

    response = requests.get("http://api.open-notify.org/astros.json")

    data = response.json()

    lst = data['people']

    if need == 'number':
        print('Number -> ', data['number'])

    elif need == 'names':
        a = 1
        for i in lst:
            print(str(a) + '.', i['name'])
            a += 1
    return ''

print(space('names'))
