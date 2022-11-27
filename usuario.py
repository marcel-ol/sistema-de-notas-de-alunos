class Usuario:
    def __init__(self):
        import psycopg2 as pg
        self.conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
        self.cursor=self.conexao.cursor()
        
    def instalaBanco(self):
        # CRIAR TABELA USUARIO
        try:     
            criarTabela = 'CREATE TABLE usuario (id SERIAL PRIMARY KEY, login VARCHAR (20) NOT NULL, senha varchar (20) NOT NULL)'
            self.cursor.execute (criarTabela)
            self.conexao.commit()
            print("Tabela USUARIO inserida.")
            #cria um novo usuario padrao
            novolog= "INSERT INTO usuario (login,senha) VALUES ('admin','1234')"
            self.cursor.execute (novolog)
            self.conexao.commit()
            print("Novo usuario incluido com sucesso!")
        except Exception as e:
            print ("Tabela USUARIO já criada. Exceção: %s" % (e))
            self.conexao.rollback()


        # CRIAR TABELA ALUNO
        try:     
            criarTabela = 'CREATE TABLE aluno (matricula BIGINT PRIMARY KEY , nome varchar (100) , av1 NUMERIC(4,2) , av2 NUMERIC(4,2) , av3 NUMERIC(4,2) , av4 NUMERIC(4,2))'
            self.cursor.execute (criarTabela)
            self.conexao.commit()
            print("Tabela ALUNO inserida.")
        except Exception as e:
            print ("Tabela ALUNO já criada. Exceção: %s" % (e))
            self.conexao.rollback()

        # CRIAR TABELA LOG
        try:     
            criarTabela = 'CREATE TABLE log (id SERIAL PRIMARY KEY , matricula BIGINT NOT NULL , login VARCHAR (20) NOT NULL, dataHora TIMESTAMP NOT NULL DEFAULT NOW(), motivo varchar (144) )'
            self.cursor.execute (criarTabela)
            self.conexao.commit()
            print("Tabela LOG inserida.")
        except Exception as e:
            print ("Tabela LOG já criada. Exceção: %s" % (e))
            self.conexao.rollback()
    def incluirUsuario(self,login,senha):
        self.conexao()
        try:
            cadastrarUsuario = 'INSERT INTO usuario (login,senha) VALUES (%s,%s)'
            self.cursor.execute (cadastrarUsuario,(login,senha))
            self.conexao.commit()
        except Exception as e:
            print ("Erro. Exceção: %s" % (e))
            self.conexao.rollback()
    def loginUsuario(self,login,senha):
        self.conexao()
        try:
            buscarUsuario = "SELECT id from usuario where login = %s and senha = %s LIMIT 1)"
            self.cursor.execute (buscarUsuario,(login,senha))
            resultado = self.cursor.fetchall()
            print ("Login realizado. Usuário %s , ID %i") % (login,resultado)
            return resultado
        except Exception as e:
            print ("Usuário não encontrado. Exceção: %s" % (e))
            self.conexao.rollback()
            return None