# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

COMM_WITHDRAWAL = 1.5
COMM_REFILL = 3
TAX = 10
COMM_MIN = 30
COMM_MAX = 600
SUM_WORK = 50
MAX_ACCOUNT = 5000000
account = 0
count_refill = 0
count_withdrawal = 0
list_money = []

# Получение суммы денег
def get_money(input_string:str)->int:

    while True:
        try:
            num = int(input(input_string))
            if num > 0 and num % SUM_WORK == 0:
                return num
            else:
                print('Сумма должна быть положительной и кратной 50')
        except ValueError:
            print('Некорретный ввод')

# добавить деньги на счет
def refil_account(num:int, list_operation:list):

    global account
    account += num
    list_operation.append(num)

# добавление 3%
def account_proc(list_operation):

    global account
    num = account / 100 * COMM_REFILL
    refil_account(num, list_operation)

# снятие денег со счета
def take_account(num:int, list_operation:list):

    global account
    account -= num
    list_operation.append(-num)

# снятие 10% на роскошь
def take_tax(list_operation):

    global account
    if account > MAX_ACCOUNT:
        num = account / 100 * TAX
        take_account(num, list_operation)

# подсчет суммы для снятия и 1,5%
def chek_money(num):

    proc = num / 100 * COMM_WITHDRAWAL
    if proc < COMM_MIN:
        num += COMM_MIN
    elif proc > COMM_MAX:
        num += COMM_MAX
    else:
        num += proc
    return num

print('Здравствуйте.Это программа банкомат\n')
while True:
    choice = int(input('Выберите желаемое действие:\n'\
      '1 - Пополнить счет\n'\
      '2 - Снять деньги со счета\n'\
      '3 - Выход\n'))
    take_tax(list_money)
    match choice:
        case 1:
            number = get_money('Введите сумму для зачисления на счет:\n')
            refil_account(number, list_money)
            count_refill += 1
            if count_refill == 3:
                account_proc(list_money)
                count_refill = 0
            print(f'У вас на счету: {account} рублей')
            print(list_money)
        case 2:
            number = get_money('Введите сумму для снятия со счета:\n')
            number = chek_money(number)
            if number < account:
                take_account(number, list_money)
                count_withdrawal += 1
                if count_withdrawal == 3:
                    account_proc(list_money)
                    count_withdrawal = 0
            else:
                print('Недостаточно средств')
            print(f'У вас на счету: {account} рублей')
            print(list_money)
        case 3:
            print('До свидания')
            print(f'У вас на счету: {account} рублей')
            print(list_money)
            break
        case _:
            print('Некорретный ввод')