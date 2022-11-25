from usuario import usuario
usuario.instalaBanco()
print("Sistema de notas")
print("=================================")
print("1: Incluir novo usuário")
print("2: Efetuar login")
print("Outra: Encerrar o sistema")
opcao = input("O que deseja fazer?")
if opcao in (1,2):
    login = input("Digite o login: ")
    senha = input("Digite o senha: ")
    if opcao == 1:
        usuario.incluirUsuario(login,senha)
    else:
        pass
else:
    print ("Seu ridículo! Escolha uma das opções disponíveis. Saindo...")
    exit()

