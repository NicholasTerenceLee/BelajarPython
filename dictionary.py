dict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

x = dict['brand']
print(x)
print(dict)

x = dict.get('model')
print(x)
print(dict)

dict['color'] = 'red'
print(x)
print(dict)

dict.update({'year' : 2020})
print(x)
print(dict)

dict['year'] = 2021
print(x)
print(dict)

dict.pop('model')
print(x)
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())