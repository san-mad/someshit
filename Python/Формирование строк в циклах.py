#Еще циклы можно использовать, чтобы формировать строки. Подобная задача часто встречается в веб-программировании. 
#Она сводится к обычной агрегации, когда применяется интерполяция или конкатенация.

#Переворот строки — алгоритмическая задача, которую задают на собеседованиях. 
# Правильный способ перевернуть строку — использовать функцию из стандартной библиотеки. Но важно знать, как ее реализовать.

#Один из алгоритмов выглядит так:

    #Строим новую строку

    #Перебираем символы исходной строки в обратном порядке
'''
def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string

reverse_string('Game Of Thrones')  # 'senorhT fO emaG'
# Проверка нейтрального элемента
reverse_string('')  # ''
'''
#Разберем функцию построчно:



    #index = len(string) - 1 — записываем в новую переменную индекс последнего символа строки (индексы начинаются с нуля)
    
    #reversed_string = '' — инициализируем строку, куда будем записывать результат
    
    #while index >= 0: — условие: повторяем тело цикла, пока текущий индекс не дошел до 0 — до первого символа
    
    #current_char = string[index] — берем из строки символ по текущему индексу
    
    #reversed_string = reversed_string + current_char — записываем в строку-результат новое значение: текущая строка-результат + новый символ
    
    #index = index - 1 — обновляем счетчик
    
    #return reversed_string — когда цикл завершился, возвращаем строку-результат



#Task
def my_substr(string, length):
    index = 0
    result = ''
    
    while index < length and index < len(string):
        current_char = string[index]
        result = result + current_char
        index = index + 1
    return result