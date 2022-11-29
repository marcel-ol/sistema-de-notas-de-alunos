class Aluno:
    def __init__(self):
        import psycopg2 as pg
        self.conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
        self.cursor=self.conexao.cursor()

    def buscarAluno(self,escolha,termo):
        try:
            if len(termo) == 0: raise Exception("Digite algum termo para buscar.")
            if escolha == 1: #busca por matricula
                buscaAluno = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE matricula = " + str(termo) + " limit 1"
            elif escolha == 2: #busca por nome
                buscaAluno = "SELECT matricula,nome,av1,av2,av3,av4 FROM aluno WHERE nome LIKE '%" + str(termo) + "%' limit 1"
            self.cursor.execute (buscaAluno)
            resultado = self.cursor.fetchone()
        except:
            self.conexao.rollback()
            resultado = 1
        return resultado

    def incluirAluno(self,idUsuario,nome,matricula,av1,av2,av3,av4):
        motivo = None
        try:
            salvaNota = "INSERT INTO aluno (matricula,nome,av1,av2,av3,av4) VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute (salvaNota,(matricula,nome,av1,av2,av3,av4))
            self.conexao.commit()
            self.gravaLog(matricula,idUsuario,"Inclusão de aluno")
            return -1
        except:
            self.conexao.rollback()
            return 1

    def alterarAluno(self,idUsuario,matricula,av1,av2,av3,av4,motivo):
        try:
            atualizaNota = "UPDATE aluno SET av1 = %s, av2 = %s, av3 = %s, av4 = %s WHERE matricula = %s"
            self.cursor.execute (atualizaNota,(av1,av2,av3,av4,matricula))
            self.conexao.commit()
            self.gravaLog(matricula,idUsuario,motivo)
            return -1
        except:
            self.conexao.rollback()
            return 1

    def gravaLog(self,matricula,idUsuario,motivo):
        try:
            novolog= "INSERT INTO log (matricula,login,motivo) VALUES (%s,%s,%s)"
            self.cursor.execute (novolog,(matricula,idUsuario,motivo))
            self.conexao.commit()
        except:
            self.conexao.rollback()

    def listarAluno(self):
        try:
            listaAluno = "SELECT matricula,nome,CAST((av1+av2+av3+av4)/4 AS NUMERIC(4,2)) AS media , CASE WHEN (av1+av2+av3+av4)/4 >= 6 THEN 'APROVADO' WHEN (av1+av2+av3+av4)/4 >= 4 THEN 'EXAME' ELSE 'REPROVADO' END AS flagAprovado FROM aluno"
            self.cursor.execute (listaAluno)
            resultado = self.cursor.fetchall()
        except:
            self.conexao.rollback()
            resultado = 1
        return resultado