from usuario import Usuario
usuario = Usuario()
usuario.instalaBanco()

print("Sistema de notas")
print("=================================")
print("1: Incluir novo usuário")
print("2: Efetuar login")
print("Outra: Encerrar o sistema")
opcao = input("O que deseja fazer?")
if opcao == "1":
    print("opcao 1")
    login = input("Digite o novo login: ")
    senha = input("Digite a nova senha: ")
    usuario.incluirUsuario(login,senha)
elif opcao == "2":
    print("opcao 2")
    login = input("Digite o login: ")
    senha = input("Digite o senha: ")
    # usuario.loginUsuario(login,senha)
else:
    print ("Seu ridículo! Escolha uma das opções disponíveis. Saindo...")
    exit()