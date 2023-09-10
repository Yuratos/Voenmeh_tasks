print(f"этот алгоритм вычисляет значение по функции: x*y*z*a^(1/2)\n"
      f"                                           ----------------\n"
      f"                                           |b|*c*(d)^(1/3)")

x = int(input(f'введите x: '))
y = int(input(f'введите y: '))
z = int(input(f'введите z: '))
a = int(input(f'введите a: '))
b = int(input(f'введите b: '))
c = int(input(f'введите c: '))
d = float(input(f'введите d: '))

f = x * y * z * a ** 0.5
F = abs(c)*c*d**1/3
print(f'результат: {f/F}')