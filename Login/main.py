import getpass

def program():
    print('--------------------Login--------------------')
    options = int(input('Digite 0 para cadastrar ou 1 para continuar para o Login: '))

    if options == 0:
        new_user = input('Crie um usuário: ')
        new_password = getpass.getpass('Crie uma senha: ')
        new_password_confirmation = getpass.getpass('Confirme sua senha: ')
        user_data = ['user:({}) password:({}) \n'.format(new_user, new_password)]

        with open('database.txt', 'a') as file:
            for data in user_data:
                file.write(data)
        
        if new_password != new_password_confirmation:
            print('A senha criada é diferente da senha digitada na confirmação. Tente novamente.')
            program()
        else:
            print("Usuário cadastrado com sucesso!")
    
    user = input("Usuário: ")
    password = getpass.getpass("Senha: ")
    with open('database.txt', 'r') as file:
        data = file.read()
        if data.find('user:({}) password:({})'.format(user, password)) != -1:
            print('Bem Vindo {}!'.format(user))
        else:
            print('O Usuário e/ou senha estão incorretos.')
        
program()