from lib.interface import *
from lib.register import *
from os import system

system("")
people_list = []

while True:
    title('CADASTRO DE PESSOAS', 45)
    mainMenu(['Cadastrar Pessoas', 'Ver Pessoas Cadastradas', 'Sair'])
    num = inputInt('>>> ')

    if num == 1:
        system('cls')
        title('CADASTRE UMA PESSOA', 45)
        register(people_list)
        system('cls')
    elif num == 2:
        system('cls')
        title('LISTA DE PESSOAS', 90)
        seeRegisters(people_list)
    elif num == 3:
        break
    else:
        system('cls')
        print('\033[31mERRO! Digite um número valido!\033[m')
print('Até mais! Vejo você em breve.')