
'''


#  Eсли есть функция, которая проверяет четность числа, то с помощью отрицания можно выполнить проверку нечетности:

def is_even(number):
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False
#  В примере выше мы добавили not слева от вызова функции и получили обратное действие.
#  Отрицание — инструмент, с которым можно выражать задуманные правила в коде и не писать новые функции.


'''
def is_not_palindrome(string):
    return string != string[::-1]        # сверху ретурна написать   string = string.lower() если нужно маленькие буквы
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('шалаш'))
print(is_not_palindrome('шалаш'))