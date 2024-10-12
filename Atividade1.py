usuario = [""] * 100
senha = [""] * 100
tamanho = 0
opcao = 1
while opcao != 4:
    print("MENU:")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Usuários")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        if tamanho < 100:
            nome = input("Digite seu nome: ")
            senhas = input("Digite sua senha: ")
            usuario[tamanho] = nome
            senha[tamanho] = senhas
            tamanho += 1
            print(f"Usuário cadastrado com sucesso.")
    elif opcao == 2:
        for x in range (tamanho):
            nome = input("Seja bem vindo ao CDD 4.0\n"
                         "Insira seu Login: ")
            senhas = input("Insira sua Senha: ")
            achou = 0
            if usuario[x] == nome and senha[x] == senhas:
                print(f"Seja bem vindo {nome} ao CDD 4.0")
                achou = +1
                break
            if achou == 0:
                print("Login ou senha inválido.")
    elif opcao == 3:
        if tamanho > 0 :
            print("Usuários cadastrados: ")
            for x in range(tamanho):
                print(usuario[x])
    elif opcao == 4:
        print("Saindo...")