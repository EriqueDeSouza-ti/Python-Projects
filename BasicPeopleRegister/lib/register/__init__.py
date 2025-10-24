from time import sleep

def register(list=[]):
    person_Info = {
        'Name'    : str,
        'LastName': str,
        'Age'     : int,
        'Birthday': int,
        'Cpf'     : int
    }


    while True:
        try:
            name     = str(input('Nome: ')).strip().title()
            lastName = str(input('Sobrenome: ')).strip().title()
            age      = int(input('Idade: '))
            birthday = int(input('Ano de Nascimento: '))
            cpf      = int(input('Cpf: '))
        except(TypeError, ValueError):
            print('ERRO! Por favor, tente novamente.')
        else:
            person_Info['Name']     = name
            person_Info['LastName'] = lastName
            person_Info['Age']      = age
            person_Info['Birthday'] = birthday
            person_Info['Cpf']      = cpf
            list.append(person_Info)
            break
        finally:
            print('=' * 45)
            print(f'Cadastro de {name} com sucesso!')
            print('=' * 45)
            sleep(2)
    return list


def seeRegisters(list=[]):
    print('-' * 90)
    print(f'{'Nome':<15}{'Sobrenome':<15}{'Idade':<15}{'Ano de Nas.':<15}{'CPF'}')
    print('-' * 90)
    for r in list:
        print(f' {r['Name']:<15}{r['LastName']:<15}{r['Age']:<15}{r['Birthday']:<15}{r['Cpf']}')
    print('=' * 90)