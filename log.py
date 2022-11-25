import psycopg2 as pg
class log:
    def novoLog():
        novolog= 'INSERT INTO log (matricula,login,motivo) VALUES (matricula,login,"Inclusão de nota")'
        cursor.execute (novolog)
        print("Log com ação foi incluido")