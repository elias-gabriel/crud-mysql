import mysql.connector
from mysql.connector import Error
from db_config import con


def Criar():
    try:
        for i in range(1):
            print('Criação de usuário')
            identidade = input('Digite um número de identidade:')
            nome = input('Digite um nome:')
            idade = input('Digie a idade:')
            email = input('Digite um email:')
            adicionar = (
                "INSERT INTO users(identidade, nome, idade, email) VALUES({},'{}', {}, '{}')".format(identidade,
                                                                                                     nome, idade,
                                                                                                     email))
        info = input('\nAs informações estão corretas? Identidade:{} Nome:{} Idade:{} Email:{} \ns = Sim n = Não'.format
                                                                                        (identidade,
                                                                                         nome, idade, email))
        if(info == 's'):
            adicionar_user = adicionar
            cursor = con.cursor()
            cursor.execute(adicionar_user)
            con.commit()
            print('\nUsuário adicionado com sucesso!!')
            cursor.close()
        else:
            print('Preencha os dados corretamente.')


    except Error as erro:
        print('Falha ao adicionar usuário {}'.format(erro))

if __name__=='__main__':
    Criar()

