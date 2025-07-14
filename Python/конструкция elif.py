'''

#   Функция get_type_of_sentence() различает только вопросительные и обычные предложения.
#   Добавим в нее поддержку восклицательных предложений:

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    if last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type
print(get_type_of_sentence('Who?'))

#     Мы добавили проверку восклицательных предложений — exclamation. Технически эта функция работает,
#    но вопросительные предложения трактует неверно. Еще в ней есть проблемы с точки зрения семантики:
#    Наличие восклицательного знака проверяется в любом случае, даже если уже обнаружился вопросительный знак
#    Ветка else описана для второго условия, но не для первого. Поэтому вопросительное предложение становится "normal"



#    Чтобы исправить ситуацию, воспользуемся еще одной возможностью условной конструкции:

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

#   Теперь все условия выстроились в единую конструкцию. 
#   elif означает — «если не выполнено предыдущее условие, 
#   но выполнено текущее». Получается такая схема:

    #если последняя буква ?, то 'question'
    #если последняя буква !, то 'exclamation'
    #остальные варианты — 'normal'

#   Выполнится только один из блоков кода, который относится ко всей конструкции if.


'''


'''

def who_is_this_house_to_stark(house):
    if house == 'Karstark':
        type_object = 'friend'
    elif house == 'Frey':
        type_object = 'enemy'
    else: house == 'Arryn'
    type_object = 'neutral'
    
    return f"{house} is {type_object}"

print(who_is_this_house_to_stark('Joar'))


'''

def who_is_this_house_to_starks(house_name):
    if house_name == "Karstark" or house_name == "Tully":
        return "friend"
    elif house_name == "Lannister" or house_name == "Frey":
        return "enemy"
    return "neutral"
    
    

