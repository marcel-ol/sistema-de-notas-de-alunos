import psycopg2 as pg
class log:
    def novoLog(self,matricula,login,motivo):
        #self.conexao()
        import db
        try:
            novolog= 'INSERT INTO log (matricula,login,motivo) VALUES (%s,%s,%s)'
            self.cursor.execute (novolog)
            self.conexao.commit()
        except Exception as e:
            print ("Erro. Exceção: %s" % (e))
            self.conexao.rollback()