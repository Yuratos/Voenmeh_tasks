print(f"этот алгоритм вычисляет значение по функции: x*y*z*a^(u)\n"
      f"                                           ----------------\n"
      f"                                           |b|*c*(d)^(e)")

x = float(input(f'введите x: '))
y = float(input(f'введите y: '))
z = float(input(f'введите z: '))
a = float(input(f'введите a: '))
b = float(input(f'введите b: '))
c = float(input(f'введите c: '))
d = float(input(f'введите d: '))
e = float(input(f'введите e: '))
u = float(input(f'введите u: '))
f = x * y * z * a ** u
F = abs(b)*c*d**e
print(f'результат: {f/F}')