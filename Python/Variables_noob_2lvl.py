
'''
def print_motto():
    print('Winter is coming!') #функция, которая выводит строку на экран
'''





'''
def say_hurray_three_times():
    word = 'hurray!'
    return ' '.join([word, word, word]) #метод join объединяет элементы списка в строку
'''


                                                                                     #get_last_char функция, которая возвращает последний символ строки





# Передача параметров напрямую без переменных
def get_last_char(Hexlet) -> str:
    return Hexlet[-1]  # Возвращает последний символ строки, переданной в качестве параметра
# Передача параметров через переменные
name1 = 'Hexlet'
get_last_char(name1)  # t
name2 = 'Goo'
get_last_char(name2)  # o
#Так же с числами              def get_last_digit(number: int) -> int: 
    #ИЛИ 
#                              round(10.23456, 3) # 10.235

'''
#'google'.replace('go', 'mo')  # moogle replace заменяет часть строки на другую строку(    def replace(text, from, to):   )
def truncate(text, length):
    if len(text) > length:
        return text[:length] + '...'
    return text #zaebalc2
'''