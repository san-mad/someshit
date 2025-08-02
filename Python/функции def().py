Функция — это блок кода, который выполняет конкретную задачу и может повторно использоваться.
def имя_функции(аргументы):  # объявление функции
    # тело функции (что она делает)
    return результат  # возвращает значение (необязательно)
	Примеры:
	
def greet(name):  
    return f"Привет, {name}!"  

print(greet("Анна"))  # Вывод: Привет, Анна!


Пример 2: Функция с вычислениями
python

def add(a, b):  
    result = a + b  
    return result  

sum_result = add(3, 5)  
print(sum_result)  # Вывод: 8


Функция, которая умножает число на 2
python

def double(x):
    return x * 2
	
	Функция, которая проверяет чётность числа
python

def is_even(num):
    return num % 2 == 0
	
	
	Функция, которая повторяет строку N раз
python

def repeat_string(text, n):
    return text * n