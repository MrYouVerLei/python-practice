import math

try:
    a = int(input('Введите первое натуральное число: '))
    b = int(input('Введите второе натуральное число: '))
except ValueError:
    print('Вы ввели не числа!')
    exit()

if a <= 0 or b <= 0:
    print('Вы ввели не натуральные числа!')
    exit()

def nod(a1, b1):
    while a1 != 0 and b1 != 0:
        if a1 > b1:
            a1 = a1 % b1
        else:
            b1 = b1 % a1
    return a1 + b1

print('НОД =', nod(a, b))
print('НОД =', math.gcd(a, b))