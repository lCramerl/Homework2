'''''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
'''

def summa_cifr(number):
    s = str(number).replace('.', '')
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = input('Введите число: ')
print()
try:
    n = float(n)
    print(summa_cifr(n))
except:
    print('Это не числоп')