'''


Скомбинируем в одном выражении логический оператор
«проверка равенства» == и арифметический оператор % и напишем функцию проверки четности:

def is_even(number):
    return number % 2 == 0

print(is_even(10))  # => True
print(is_even(3))   # => False


'''







'''


Теперь напишем функцию, которая принимает строку и проверяет, начинается ли эта строка с латинской буквы a.

Алгоритм:

    Получим и запишем в переменную первый символ из строки-аргумента
    Сравним, равен ли символ латинской букве a
    Вернем результат

def is_first_letter_an_a(string):
    first_letter = string[0]
    return first_letter == 'a'

print(is_first_letter_an_a('orange'))  # => False
print(is_first_letter_an_a('apple'))   # => True


'''



#Догадаешься сам, лень писать
#noob
def is_international_phone(int):
    first_symbol = (int)[0]
    return first_symbol == '+'


#pro
def is_international_phone(phone):
    return phone[0] == "+"