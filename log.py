class log:
    def novoLog():
        import db
        novolog= 'INSERT INTO log (matricula,login,motivo) VALUES (matricula,login,"Inclusão de nota")'
        cursor.execute (novolog)
        print("Log com ação foi incluido")