class log:
    def novoLog():
        conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
        novolog= "INSERT INTO log (matricula,login,motivo) VALUES (matricula,login,'Inclusão de nota')"
        cursor=conexao.cursor()
        cursor.execute (novolog)
        print("Log com ação foi incluido")