import requests
def people_in_space(need):
    '''
    Type 'number' if you wanna know a number of people in space.\
    Type 'names' if you wanna know the names of people in spase.\
    '''
    url = "http://api.open-notify.org/astros.json"
    r = requests.get(url)

    data = r.json()

    lst = data['people']

    if need == 'number':
        print('Number -> ', data['number'])
        return''

    elif need == 'names':
        a = 1
        for i in lst:
            print(str(a) + '.', i['name'])
            a += 1
        return''
