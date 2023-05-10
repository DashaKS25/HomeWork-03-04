a = int(input('Введіть fizz: '))
b = int(input('Введіть buzz: '))
c = int(input('Додайте число до якого треба порахувати: '))
numbers = []
with open('numbers.txt', 'r') as f:
  [print('FB' if(num % a == 0) and (num % b == 0) else 'F' if(num % a == 0) else'B' if(num % b == 0) else num) for num in range (1, c + 1)]
