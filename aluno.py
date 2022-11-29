class Aluno:
    def __init__(self):
        import psycopg2 as pg
        self.conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
        self.cursor=self.conexao.cursor()

    def buscarAluno(self,escolha,termo):
        try:
            if escolha == 1: #busca por matricula
                buscaAluno = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE matricula = " + str(termo) + " limit 1"
            elif escolha == 2: #busca por nome
                buscaAluno = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE nome LIKE '%" + str(termo) + "%' limit 1"
            print(buscaAluno)
            self.cursor.execute (buscaAluno)
            resultado = self.cursor.fetchone()
        except Exception as e:
            print ("Erro na busca. Exceção: %s" % (e))
        print("resultado = ",resultado)
        return resultado

    def incluirAluno(self,idUsuario,nome,matricula,av1,av2,av3,av4):
        motivo = None
        try:
            salvaNota = "INSERT INTO aluno (matricula,nome,av1,av2,av3,av4) VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute (salvaNota,(matricula,nome,av1,av2,av3,av4))
            self.conexao.commit()
            print(f"Aluno {nome} inserido.")
            self.gravaLog(matricula,idUsuario,"Inclusão de aluno")
            return -1
        except Exception as e:
            print ("Erro na inclusão. Exceção: %s" % (e))
            self.conexao.rollback()
            return 1


    def gravaLog(self,matricula,idUsuario,motivo):
        try:
            novolog= "INSERT INTO log (matricula,login,motivo) VALUES (%s,%s,%s)"
            self.cursor.execute (novolog,(matricula,idUsuario,motivo))
            self.conexao.commit()
            print("Ação gravada no Log.")
            if(motivo != None):
                return -1
            else: return 2
        except Exception as e:
            print ("Erro na gravação do log. Exceção: %s" % (e))
            self.conexao.rollback()
            return 3

    def alterarAluno(self,idUsuario,nome,matricula,av1,av2,av3,av4,motivo):
        try:
            atualizaNota = "UPDADE aluno SET av1 = %s, av2 = %s, av3 = %s, av4 = %s WHERE matricula = %s)"
            self.cursor.execute (atualizaNota,(av1,av2,av3,av4,matricula))
            self.conexao.commit()
            print(f"Nota(s) do aluno {nome} alterada(s).")
        except Exception as e:
            print ("Erro na alteração. Exceção: %s" % (e))
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
            print ("Erro na gravação do log. Exceção: %s" % (e))
            self.conexao.rollback()
            return 3