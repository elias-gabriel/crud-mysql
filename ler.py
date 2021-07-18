import mysql.connector
from mysql.connector import Error
from db_config import con

def consulta(IdUser):
    try:
        IdUser = input('\nQual o ID do usuário?')
        consulta_sql = 'SELECT * FROM users WHERE identidade = ' + IdUser
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print('IDENTIDADE:', linha[0])
            print('NOME:', linha[1])
            print('IDADE:', linha[2])
            print('EMAIL:', linha[3])
    except Error as erro:
        print('Falha ao consultar a tabela: {}'.format(erro))
