class Aluno:
    def __init__(self):
        import psycopg2 as pg
        self.conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
        self.cursor=self.conexao.cursor()
        # print ("Controle de Aluno")
        # print("=================================")
        # print("1: Buscar Aluno")
        # print("2: Incluir novo aluno")
        # print("3: Alterar Aluno")
        # escolha = input("Escolha uma opção:")
        # if escolha == "1":
        #     self.buscarAluno()
        # elif escolha == "2":
        #     self.incluirAluno()
        #self.incluirAluno()

    def buscarAluno(self,escolha,termo):
        if escolha == 1:
            # matricula = input("Qual a matricula do aluno:")
            buscaNota = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE matricula = " +termo+ " limit 1"
            self.cursor.execute (buscaNota) #,matricula)
            resultado = self.cursor.fetchone()

        elif escolha == 2:
            # nome = input("Qual o nome do aluno:")
            buscaNota = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE nome LIKE '%" +termo+ "%' limit 1"
            self.cursor.execute (buscaNota) #,matricula)
            resultado = self.cursor.fetchone()
        print (resultado)
        return resultado

    def incluirAluno(self,idUsuario,nome,matricula,av1,av2,av3,av4):
        motivo = None
        try:
            salvaNota = "INSERT INTO aluno (matricula,nome,av1,av2,av3,av4) VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute (salvaNota,(matricula,nome,av1,av2,av3,av4))
            self.conexao.commit()
            print(f"Aluno {nome} inserido.")
            motivo = "Inclusão de aluno"
        except Exception as e:
            print ("Erro na inclusão. Exceção: %s" % (e))
            self.conexao.rollback()
            return 1

        try:
            novolog= "INSERT INTO log (matricula,login,motivo) VALUES (%s,%s,%s)"
            self.cursor.execute (novolog,(matricula,idUsuario,motivo))
            self.conexao.commit()
            print("Ação gravada no Log.")
            if(motivo != None):
                return -1
            else: return 2
        except Exception as e:
            print ("Erro encontrado. Exceção: %s" % (e))
            self.conexao.rollback()
            return 3