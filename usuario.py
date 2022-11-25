class usuario:
    def conexao(self):
        # Conectar ao banco de dados. 
        self.conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
        self.cursor=conexao.cursor()
    def criarTabelas(self):
            self.conexao()
            # CRIAR TABELA ALUNO
            try:     
                # Executando um comando DDL - Data Definiton Language 
                criarTabela = 'create table aluno (matricula INT PRIMARY KEY , nome varchar (100) , av1 NUMERIC(4,2) , av2 NUMERIC(4,2) , av3 NUMERIC(4,2) , av4 NUMERIC(4,2))'
                # Executar a query DML 
                self.cursor.execute (criarTabela)
                # Efetivar a criação. sem esta linha a Tabela não será Serializada no disco. 
                self.conexao.commit()
            except Exception as e:
                print ("Tabela ALUNO já criada.")
                self.conexao.rollback()
            # CRIAR TABELA LOGIN
            try:     
                # Executando um comando DDL - Data Definiton Language 
                criarTabela = 'create table notas (matricula INT PRIMARY KEY , nome varchar (100) , av1 NUMERIC(3,1) , av2 NUMERIC(3,1) , av3 NUMERIC(3,1) , av4 NUMERIC(3,1))'
                # Executar a query DML 
                self.cursor.execute (criarTabela)
                # Efetivar a criação. sem esta linha a Tabela não será Serializada no disco. 
                self.conexao.commit()
            except Exception as e:
                print ("Tabela já criada.")
                self.conexao.rollback()