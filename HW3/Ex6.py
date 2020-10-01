# Задание 6.1.

def int_func(word):
    #return word.title()
    word = word.lower()
    result = word[0].upper() + word[1::]
    return result

print(f'Слово с заглавной буквы: {int_func("colorleSs")}.')

# Задание 6.2.

def int_func(string):
    #return string.title()
    string = string.lower()
    result = []
    for word in string.split():
        result.append(word[0].upper() + word[1::])
    return ' '.join(result)

print(f'Слова с заглавной буквы: {int_func("colorless green ideas sleep furiously")}.')