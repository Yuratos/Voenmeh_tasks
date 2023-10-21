# Задается целое число с клавиатуры
# преобразовать число в римские цифры
print('этот алгоритм преобразует арабские числа в римские')
num = int(input('введите любое целое число:'))
def arabic_to_romanian (num): #функция преобразования арабского числа в римское
    romainian_numerals = { #создание словаря ключ: 'значение'
        5000: '~V',
        1000: 'M' ,
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        50: 'L',
        40: 'XL',
        90: 'XC',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    romanian_num = ''#пустая переменная для записи римского числа
    for value, symbol in romainian_numerals.items(): #проходимся по каждой паре ключ: 'значение' 
        while num >= value:#пока арабское число больше или равно текущего значения из словаря:
            romanian_num += symbol #добавляем римский символ
            num -= value#вычитаем арабский символ из числа
    return romanian_num
roman_number = arabic_to_romanian(num)#вызов функции
print(f'число {roman_number} ')
