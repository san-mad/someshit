def is_arguments_for_substr_correct(string, index, length):
    if not isinstance(string, str):
        return False
    if not isinstance(index, int) or not isinstance(length, int):
        return False
    if length < 0:
        return False
    if index < 0:
        return False
    if index >= len(string):
        return False
    if index + length > len(string):
        return False
    return True


'''
Функция-предикат is_arguments_for_substr_correct(), которая принимает три аргумента:

    строку;
    индекс, с которого начинать извлечение;
    длину извлекаемой подстроки.

Функция возвращает False, если хотя бы одно из условий истинно:

    Отрицательная длина извлекаемой подстроки.
    Отрицательный заданный индекс.
    Заданный индекс выходит за границу всей строки.
    Длина подстроки в сумме с заданным индексом выходит за границу всей строки.
'''