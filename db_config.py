import mysql.connector
from mysql.connector import Error

con = mysql.connector.connect(host='localhost', user='root', password='miranha123', database='crud',
                                          charset='utf8')