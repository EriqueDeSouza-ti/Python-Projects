def title(msg=str, length=int):
    print('=' * length)
    print(msg.center(length))
    print('=' * length)
    return length

def mainMenu(list=[]):
    for i, item in enumerate(list, start=1):
        print(f'\033[33m{i} \033[m- \033[34m{item.upper()}\033[m')

def inputInt(msg=str):
    print('=' * 45)
    while True:
        try:
            value = int(input(f'\033[32m{msg}\033[m'))
        except(ValueError, TypeError):
            print('\033[31mERRO! Por favor, tente novamente!\033[m')
        else:
            break
    print('=' * 45)
    return value