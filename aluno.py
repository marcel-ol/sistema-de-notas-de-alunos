import psycopg2 as pg

class Aluno:
    conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
    cursor=conexao.cursor()

    def __init__(self):
        print ("Controle de Aluno")
        print("=================================")
        print("1: Buscar Aluno")
        print("2: Incluir novo aluno")
        print("3: Alterar Aluno")
        escolha = input("Escolha uma opção:")
        if escolha == "1":
            self.buscarAluno()
        elif escolha == "2":
            self.incluirAluno()
        #self.incluirAluno()

    def buscarAluno(self):
        login = "admin"
        print("\tBuscar Aluno")
        print("=================================")
        print("1: Buscar aluno pela matricula")
        print("2: Buscar aluno pelo nome")
        escolha = input("Escolha uma opção:")

        if escolha == "1":
            matricula = input("Qual a matricula do aluno:")
            buscaNota = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE matricula = " +matricula+ " limit 1"
            self.cursor.execute (buscaNota) #,matricula)
            resultado = self.cursor.fetchone()
            print (resultado)

        elif escolha == "2":
            nome = input("Qual o nome do aluno:")
            buscaNota = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE nome LIKE '%" +nome+ "%' limit 1"
            self.cursor.execute (buscaNota) #,matricula)
            resultado = self.cursor.fetchone()
            print (resultado)
        else:
            print("Escolha um opção valida")

    def incluirAluno(self):
        login = "admin"
        print("\n\n")
        print("\tInserir novo aluno")
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
            try:
                salvaNota = "INSERT INTO aluno (matricula,nome,av1,av2,av3,av4) VALUES (%s,%s,%s,%s,%s,%s)"
                self.cursor.execute (salvaNota,(matricula,nome,av1,av2,av3,av4))
                self.conexao.commit()
                print(f"Nota do aluno {nome} foi inserida.")
                aviso = "Inclusão de nota"
            except Exception as e:
                print ("Matricula ja wexiste. Exceção: %s" % (e))
                self.conexao.rollback()

            try:
                novolog= "INSERT INTO log (matricula,login,motivo) VALUES (%s,%s,%s)"
                self.cursor.execute (novolog,(matricula,'Admin',aviso))
                self.conexao.commit()
                print("Log com ação foi incluido")
            except Exception as e:
                print ("Erro encontrado. Exceção: %s" % (e))
                self.conexao.rollback()

#Primeira linha a ser executada
obj = Aluno()
# obj.mainloop()
