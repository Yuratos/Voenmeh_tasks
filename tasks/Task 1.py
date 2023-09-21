print(f"этот алгоритм вычисляет значение по функции: x*y*z*a^(u)\n"
      f"                                           ----------------\n"
      f"                                           |b|*c*(d)^(e)")

x = float(input(f'введите x: '))  # c 5 по 13 строку вводим числа и степени
y = float(input(f'введите y: '))
z = float(input(f'введите z: '))
a = float(input(f'введите a: '))
b = float(input(f'введите b: '))
c = float(input(f'введите c: '))
d = float(input(f'введите d: '))
e = float(input(f'введите e: '))
u = float(input(f'введите u: '))
f = x * y * z * a ** u  # формула числителя
F = abs(b) * c * d ** e  # формула знаменателя
print(f'результат: {f / F}')
