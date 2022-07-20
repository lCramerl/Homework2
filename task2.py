'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

def multiplication(k):
    if k == 1:
       return 1
    else:
        return k*multiplication(k-1)


n = input('Введите число: ')
print()
try:
    n = int(n)
    list = []
    for i in range(1, n+1):
        list.append(multiplication(i))
    print(list)
except:
    print("Это не явлется целым числом!")