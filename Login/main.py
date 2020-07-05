import getpass
from cryptography import cryptograph

def Login():
    print('--------------------Login--------------------')
    options = int(input('Digite 0 para cadastrar ou 1 para logar: '))

    if options == 0:
        # Coleta de dados
        new_user = input('Crie um usuário: ')

        # Tratamento de erro - usuário já existe
        with open('database.txt', 'r') as file:
            data = file.read()
            if data.find('user:({})'.format(new_user)) != -1:
                print("O usuário digitado já existe. Tente novamente.")
                exit()
        new_password = getpass.getpass('Crie uma senha (apenas letras e números e sem espaços): ')

        # Tratamento de erro - caracter inválido
        for character in new_password:
            if character in [
                "!","@","#","$","%","^","&","*","(",")","_","+","-",
                "=",'{','}',')','(','¨','^','~','.',',','?',';',':',
                '>','<',"'",'"','-','_','§','°','/','|', ' '
            ]:
                print("A senha digitada não é válida. Tente novamente.")
                exit()
            else:
                pass

        new_password_confirmation = getpass.getpass('Confirme sua senha: ')

        # Tratamento de erro - senhas diferentes
        if new_password != new_password_confirmation:
            print('A senha criada é diferente da senha digitada na confirmação. Tente novamente.')
            exit()
        else:
            print("Usuário cadastrado com sucesso!")

        user_data = ['user:({}) password:({}) \n'.format(new_user, cryptograph(new_password))]

        # Cadastro no banco de dados
        with open('database.txt', 'a') as file:
            for data in user_data:
                file.write(data)

    else:
        user = input("Usuário: ")
        password = getpass.getpass("Senha: ")
        with open('database.txt', 'r') as file:
            data = file.read()
            if data.find('user:({}) password:({})'.format(user, cryptograph(password))) != -1:
                print('Bem Vindo {}!'.format(user))
            else:
                print('O Usuário e/ou senha estão incorretos.')
        
Login()