import psycopg2 as pg
conexao = pg.connect(host='127.0.0.1', database='postgres', user='postgres', password='1234')
cursor=conexao.cursor()