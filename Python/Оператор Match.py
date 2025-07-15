#Оператор match — это специализированная версия if, 
# которую создали для особых ситуаций. Например, ее нужно использовать там,
# где есть цепочка if else с проверками на равенство:

# Пример с использованием match-case (Python 3.10+)
'''
   match status:
    case 'processing':
        pass
    case 'paid':
        pass
    case 'new':
        pass
    case _:
        pass
        
        '''    
        
#    Функция match принимает значение, которое нужно проверить,(thx copilot)
        
        
def get_number_explanation(number):
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'
