import mysql.connector
from mysql.connector import Error
from db_config import con

def consulta(IdUser):
    try:
        con
        # IdUser = input('Qual o ID do usuário?')
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
    # finally:
    # if(con.is_connected()):
    # cursor.close()
    # con.close()


def Deletar():
    try:
        print('Remover Usuário do DB')
        print('\nDigite o id do usuário que será removido:')

        IdUser = input('ID do usuário:')
        delecao = "DELETE from users WHERE identidade = " + IdUser

        consulta(IdUser)
        verifica = input('DESEJA DELETAR O USUÁRIO? s = sim, n = não')
        if (verifica == 's'):
            deletar_user = delecao
            cursor = con.cursor()
            cursor.execute(deletar_user)
            con.commit()
            print('Usuário deletado com sucesso!!')
            cursor.close()
        else:
            print('\nAté logo')


    except Error as erro:
        print('Falha ao deletar usuário: {}'.format(erro))

if __name__ == '__main__':
    Deletar()