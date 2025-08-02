password = input("Введите пароль: ")
if password == str("123456"):
    print("Пароль принят")
else:
    print("Неверный пароль")
#короче хуеня ебаная ваша тернарная операция

for symbol in password:
    if symbol == '1':
        print("Символ 1 найден в пароле")
    elif symbol == '2':
        print("Символ 2 найден в пароле")
    elif symbol == '3':
        print("Символ 3 найден в пароле")
    else:
        print("Другой символ найден в пароле")