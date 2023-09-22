print(f"этот алгоритм вычисляет значение по функции: x*y*z*a^(1/2)\n"
      f"                                           ----------------\n"
      f"                                           |b|*c*(d)^(1/3)")

x = float(input(f'введите x: '))  # c 5 по 13 строку вводим числа и степени
y = float(input(f'введите y: '))
z = float(input(f'введите z: '))
a = float(input(f'введите a: '))
b = float(input(f'введите b: '))
c = float(input(f'введите c: '))
d = float(input(f'введите d: '))
e = float(input(f'введите e: '))
f = x * y * z * a ** (1./2.)  # формула числителя
F = abs(b) * c * d ** (1./3.)  # формула знаменателя
print(f'результат: {f / F}')
