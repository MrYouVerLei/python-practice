import math

try:
    a = int(input('Введите первое натуральное число: '))
    b = int(input('Введите второе натуральное число: '))
except ValueError:
    print('Вы ввели не числа!')
    exit()

if a <= 0 or b <= 0:
    print('Вы ввели не натуральные числа! Попробуйте ещё раз.')
    exit()

def nod(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y

print('НОД функции =', nod(a, b))
print('НОД с помощью модуля "math" =', math.gcd(a, b))