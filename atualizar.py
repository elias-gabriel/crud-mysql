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


def atualiza():
    try:
        print('Atualizar dados do usuário no DB')
        print('\nDigite o ID do usuário ao alterar a idade:')

        IdUser = input('ID do usuário:')
        consulta(IdUser)

        print('Digite a nova idade do usuário')
        NovaIdade = input('NOVA IDADE: ')

        atualizacao = """UPDATE users SET idade = """ + NovaIdade + """ WHERE identidade = """ + IdUser
        cursor = con.cursor()
        cursor.execute(atualizacao)
        con.commit()
        print('Idade alterada com sucesso!')

        verifica = input('DESEJA CONSULTAR A ATUALIZAÇÃO? s = sim, n = não')
        if (verifica == 's'):
            consulta(IdUser)
        else:
            print('\nAté logo!')

    except Error as erro:
        print('Falha ao inserir dados na tabela: {}'.format(erro))

if __name__ == '__main__':
    atualiza()