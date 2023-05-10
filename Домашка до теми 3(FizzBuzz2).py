#Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
a = int(input('Введіть fizz: '))
b = int(input('Введіть buzz: '))
c = int(input('Додайте число до якого треба порахувати: '))
numbers = []
with open('numbers.txt', 'r') as f:

    for num in range(1, c+1):
        if num % a == 0 and num % b == 0:
            print('FB', end = ' ')
        elif num % a == 0:
            print('F', end = ' ')
        elif num % b == 0:
            print('B', end = ' ')
        else:
            print(num, end = ' ')