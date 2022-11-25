class aluno:
    def novaNota():
        import db
        login = "admin"
        print("Cadastro de notas")
        print("=================================")
        print("Digite abaixo com atenção as notas do aluno")
        matricula = input("Matricula do aluno?")
        nome = input("Nome do aluno:")
        av1 = input("Nota da AV1:")
        av2 = input("Nota da AV2:")
        av3 = input("Nota da AV3:")
        av4 = input("Nota da AV4:")

        if (matricula == ""):
            print("Digite a porra de uma matricula !")
        elif(nome == ""):
            print("Digite a desgraça do nome do aluno:")
        elif(av1 == ""):
            print ("Nota da AV1 é obrigatoria")
        elif(av2 == ""):
            print ("Nota da AV2 é obrigatoria")
        elif(av3 == ""):
            print ("Nota da AV3 é obrigatoria")
        else:
            salvaNota= 'INSERT INTO aluno (matricula,nome,av1,av2,av3,av4) VALUES (%s,%s,%s,%s,%s,%s)'
            cursor.execute (salvaNota)
            conexao.commit()
            print(f"Nota do aluno {nome} foi inserida.")

            novolog= 'INSERT INTO log (matricula,login,motivo) VALUES (matricula,login,"Inclusão de nota")'
            cursor.execute (novolog)
            print("Log com ação foi incluido")