# Создать текстовый файл
# Взять текст из первого файла,
# каждая третья буква переходит на верхний регистр
# Каждая вторая буква меняется на первую
# Записать получившийся текст во второй файл

with open('2.txt', mode='r', encoding='utf-8') as myfile:  # присваивание переменной 'myfile' открытие файла
    text = myfile.read()  # присваивание переменной чтение файла
    print(text)  # выводим исходный текст из файла '2.txt'
string = text  # Создаем переменную string и присваиваем ей значение
new_string = ""  # Создаем пустую строковую переменную new_string, которая будет использоваться для формирования
# новой строки
for i, char in enumerate(string):  # Запускаем цикл, в котором происходит итерация по каждому символу строки string с
    # помощью функции enumerate(). Переменная i содержит индекс текущего символа, а переменная char содержит сам символ
    if (i + 1) % 3 == 0:  # Проверяем условие, является ли текущий символ третьим символом в строке (индекс + 1
        # делится на 3 без остатка)
        new_string += char.upper()  # Если условие истинно, то текущий символ переводится в верхний регистр с помощью
        # метода upper() и добавляется к новой строке new_string
    elif (i + 1) % 2 == 0:  # Если предыдущее условие не выполняется, то проверяем условие, является ли текущий символ
        # вторым символом в строке (индекс + 1 делится на 2 без остатка)
        new_string += string[0]  # Если условие истинно, то в новую строку new_string добавляется первый символ из
        # исходной строки string
    else:  # Если ни одно из предыдущих условий не выполняется, то выполняется блок кода внутри else
        new_string += char  # Текущий символ добавляется к новой строке new_string без изменений

print(new_string)  # Выводим новую строку new_string на экран
myfile.close()
with open('task_2.result.txt', mode='r+', encoding='utf-8')as yourfile:
    yourfile.write(new_string)
yourfile.close()