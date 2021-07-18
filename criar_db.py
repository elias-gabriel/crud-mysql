import mysql.connector

con = mysql.connector.connect(host='localhost', user='', passwd='', port=3306 )
cursor = con.cursor()

criar_tabelas = '''SET NAMES latin1;
    DROP DATABASE IF EXISTS CRUD;
    CREATE DATABASE `CRUD` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `CRUD`;
    CREATE TABLE `users` (
      `identidade` int(11) NOT NULL,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `idade` int(3) NOT NULL,
      `email` varchar(40) NOT NULL,
      PRIMARY KEY (`identidade`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    '''

for result in cursor.execute(criar_tabelas, multi=True):
    print(cursor.rowcount)

cursor.executemany(
      'INSERT INTO CRUD.users (identidade, nome, idade, email) VALUES (%s, %s, %s, %s)',
      [
            ('1', 'Elias Gabriel', '16', 'elias@gmail.com'),
      ])

con.commit()

print('\nDados Inseridos com sucesso!\n')

dados = 'SELECT * FROM CRUD.users'
cursor.execute(dados)
linhas  = cursor.fetchall()
for linha in linhas:
    print('IDENTIDADE:', linha[0])
    print('NOME:', linha[1])
    print('IDADE:', linha[2])
    print('EMAIL:', linha[3])

cursor.close()