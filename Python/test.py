# значение - values(USA;883305;Bridge)
# ключи - keys(country;population;name)
# словарь - dictionary
information = {'country': 'USA' ,'population' : 883305 ,'name': 'Bridge'}
key = (input('Enter a key to retrieve its value:\n'))
if key == 'country':
    print(information.get('country'))
elif key == 'population':
    print(information.get('population'))
elif key == 'name':
    print(information.get('name'))
else:
    print('Key not found in the dictionary.')
