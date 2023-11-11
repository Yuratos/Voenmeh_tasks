class SELECTOR:

    def fibonacci(self):
        from functools import lru_cache

        @lru_cache()
        def reverse_fib_cached(n):
            if n == 1 or n == 2:
                return 1

            return reverse_fib_cached(n - 1) + reverse_fib_cached(n - 2)

        n = int(input('enter n'))
        result = reverse_fib_cached(n)
        print(n, '--', result, 'press "q" to return to menu ')
        if input() == 'q':

            return self.menu()
    def romanian_converter(self):
        # Задается целое число с клавиатуры
        # преобразовать число в римские цифры
        print('этот алгоритм преобразует арабские числа в римские')
        num = int(input('введите любое целое число:'))

        def arabic_to_romanian(num):  # функция преобразования арабского числа в римское
            romainian_numerals = {  # создание словаря ключ: 'значение'
                5000: '~V',
                1000: 'M',
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
            romanian_num = ''  # пустая переменная для записи римского числа
            for value, symbol in romainian_numerals.items():  # проходимся по каждой паре ключ: 'значение'
                while num >= value:  # пока арабское число больше или равно текущего значения из словаря:
                    romanian_num += symbol  # добавляем римский символ
                    num -= value  # вычитаем арабский символ из числа
            return romanian_num

        roman_number = arabic_to_romanian(num)  # вызов функции
        print(f'число {roman_number} ' 'press "q" to return to menu ')
        if input() == 'q':
            return self.menu()
    def letters_replacer(self):
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
        for i, char in enumerate(
                string):  # Запускаем цикл, в котором происходит итерация по каждому символу строки string с
            # помощью функции enumerate(). Переменная i содержит индекс текущего символа, а переменная char содержит сам символ
            if (i + 1) % 3 == 0:  # Проверяем условие, является ли текущий символ третьим символом в строке (индекс + 1
                # делится на 3 без остатка)
                new_string += char.upper()  # Если условие истинно, то текущий символ переводится в верхний регистр с помощью
                # метода upper() и добавляется к новой строке new_string
            elif (
                    i + 1) % 2 == 0:  # Если предыдущее условие не выполняется, то проверяем условие, является ли текущий символ
                # вторым символом в строке (индекс + 1 делится на 2 без остатка)
                new_string += string[
                    0]  # Если условие истинно, то в новую строку new_string добавляется первый символ из
                # исходной строки string
            else:  # Если ни одно из предыдущих условий не выполняется, то выполняется блок кода внутри else
                new_string += char  # Текущий символ добавляется к новой строке new_string без изменений

        print(new_string)  # Выводим новую строку new_string на экран
        myfile.close()
        with open('task_2.result.txt', mode='r+', encoding='utf-8') as yourfile:
            yourfile.write(new_string)
        yourfile.close()
        print('file 2 succesfuly rewrited, press "q" to return to menu ')
        if input() == 'q':
            return self.menu()

    def calculator(self):
        print(f"этот алгоритм вычисляет значение по функции: x*y*z*a^(1/2)\n"
              f"                                           ----------------\n"
              f"                                           |b|*c*(d)^(1/3)"
              f"                                  \n"
              f"                                Для перехода в меню введите 'Q'")

        x = float(input(f'введите x: '))  # c 5 по 13 строку вводим числа и степени
        y = float(input(f'введите y: '))
        z = float(input(f'введите z: '))
        a = float(input(f'введите a: '))
        b = float(input(f'введите b: '))
        c = float(input(f'введите c: '))
        d = float(input(f'введите d: '))
        e = float(input(f'введите e: '))
        f = x * y * z * a ** (1. / 2.)  # формула числителя
        F = abs(b) * c * d ** (1. / 3.)  # формула знаменателя
        print( f'результат: {f / F}', 'press "q" to return to menu ')
        if input() == 'q':
                return self.menu()



    def menu(self):
        t = str(input(f'Пожалуйтса, выберете опцию:\n '
                    f' 1 -- калькулятор по формуле\n'
                    f' 2 -- редактировнаие текста в файле\n'
                    f' 3 -- перевод в римские числа\n'
                    f' 4 -- числа фибоначи\n'
                    f' q -- выход из меню\n'))
        while t != 'q':
            if t == '1':
                return self.calculator()
            elif t == '2':
                return self.letters_replacer()
            elif t == '3':
                return self.romanian_converter()
            elif t == '4':
                return self.fibonacci()
            elif t == 'q':
                break
            else:
                print( ' error, please select exist option')
                return self.menu()

selector1 = SELECTOR()

selector1.menu()

