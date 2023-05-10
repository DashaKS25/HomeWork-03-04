amount = int(input('Введіть сумму:'))
balance =10000

def withdraw(amount):
    global balance
    if amount > balance:
        print('Невистачає коштів')
    elif amount % 10 != 0:
        print('Сума повинна бути кратна 10 гривням')
    else:
        nominals = {100: 10, 50: 10, 20: 10, 10: 10}

        result = {}
        for nominal in sorted(nominals.keys(), reverse = True):
            count = min(amount // nominal, nominals[nominal], 10)
            amount -= count * nominal
            result[nominal] = count
            nominals[nominal] -= count
        if amount != 0:
            print('Неможливо видати дрібними')
            return

        balance -= sum([nominals * count for nominals, count in result.items()])
        print('Видано грошей')
        for nominal, count in result.items():
            if count > 0:
             print(nominal, "x", count)
        print('Залишок:', balance)



withdraw(amount)
