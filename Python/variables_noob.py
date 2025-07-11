'''
euros_count = 100
euros_count = 100
dollars_count = euros_count * 1.25
print(dollars_count)
yuans_per_dollar = 6.91
yuans_count = dollars_count * yuans_per_dollar
print(yuans_count)
'''


'''
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."      

first_name = "Joffrey!"
greeting = "Hello, "
print(greeting + first_name)
print(intro + "\n" + info)


#ANOTHER OPTION
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."
first_name = "Joffrey!"
greeting = "Hello, "
print(greeting + first_name)
print(intro + "\n" + info)

'''


'''
stark = "Arya"
dinner = f'Do you want to eat, {stark}?'
print(dinner)


#ANOTHER OPTION
print(f"Do you want to eat, {stark}?")

'''




'''
name = "Na\nharis"
print(name[0]) # print(name[2:5])
'''


'''
text = """Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground."""

print(text)
'''

'''
one = "Naharis"
two = "Mormont"
three = "Sand"
result = f'{one[3]}{two[1]}{three[3]}{two[4]}{two[2]}'
print(result)



'''




'''


#Type conversion


value = 2.9
int_value = int(value)
print(f'{str(int_value)} times')


'''


'''
result = pow(2, 3)  # 2 * 2 * 2
print(result)  # => 8
'''


'''
number = 10.1234
print(round(number, 2))
'''





'''
text = "Never forget what you are, for surely the world will not"
print(f'First: {text[0]}') 
print(f'First: {text[-1]}') 
'''

'''
#Или так
text = "Never forget what you are, for surely the world will not"
result = f"First: {text[0]}\nLast: {text[-1]}"
print(result) #First: N 
              #Last:t
'''




#variables max() / min()
"""
print(f'''{min(3, 10, 22, -3, 0)}    #min => -3
 {max(1, 2, 3, 4)}''')               #max=> 4
"""







'''
#random number
from random import random
print(round(random() * 1000000))
'''





'''
#Как найти тип str/int
print(f"""{type(10)} {type('NoDota')}""")
'''




#Строковые методы
#https://docs.python.org/3/library/stdtypes.html#string-methods
'''
name = 'Python'

# Возвращает индекс первого вхождения буквы в строку
name.find('t')  # 2

# Переводит в нижний регистр           #text = "a MIND needs Books as a Sword needS a WHETSTONE."
name.lower()  # 'python'               #print(text.lower()) типа один пример

# Заменяет одну подстроку другой
name.replace('on', 'off')  # 'Pythoff'
'''





'''
#Применить метод .strip() к полученной подстроке 
# для удаления возможных пробелов или 
# скрытых символов начала и конца строки.
p = 'hello                       \n'
print(p.strip())  #hello
'''








'''
#Найти индекс символов
text = "Never forget what you are, for surely the world will not"
print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")  #N,',' = 0,25
'''











