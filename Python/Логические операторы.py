


'''
#Функция, которая принимает пароль и говорит, оответствует ли он условиям (True) или не соответствует (False):

def has_capital_letter(string):
    # Проверяет наличие хотя бы одной заглавной буквы в строке

def is_correct_password(password):
   length = len(password)
   return length > 8 and has_capital_letter(password)

print(is_correct_password('Qwerty'))                   # => False
print(is_correct_password('Qwerty1234'))               # => True
print(is_correct_password('qwerty1234'))               # => False

'''




'''



#  Операторы можно комбинировать в любом количестве и любой последовательности. 
#  Если в коде одновременно встречаются and и or, то приоритет лучше задавать скобками. 
#  Ниже пример расширенной функции, которая определяет корректность пароля:

def has_capital_letter(string):
    # Проверяет наличие хотя бы одной заглавной буквы в строке
def has_special_chars(string):
    # Проверяет содержание специальных символов в строке

def is_strong_password(password):
    length = len(password)
    # Скобки задают приоритет. Понятно, что к чему относится.
    return (length > 8 and has_capital_letter(password)) and has_special_chars(password)




#  Теперь представим, что мы хотим купить квартиру, 
#  которая удовлетворяет таким условиям: площадь от 100 квадратных метров и больше 
#  на любой улице ИЛИ площадь от 80 квадратных метров и больше, но на центральной улице Main Street.

Напишем функцию, которая проверит квартиру. Она принимает два аргумента: площадь — число и название улицы — строку:

def is_good_apartment(area, street):
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street'))  # => True
print(is_good_apartment(120, 'Main Street'))    # => True
print(is_good_apartment(80, 'Main Street'))     # => True


'''


def is_leap_year(year):
    # Проверяет, является ли год високосным
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)