import mysql.connector
import time
con = mysql.connector.connect(host='localhost',database='Confeitaria',user='root',password='')





if con.is_connected():
    db_info = con.get_server_info()
    print("\nConectado ao servidor MySQL versão ",db_info)

    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    time.sleep(2)

    print("\nConectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    time.sleep(2)
    print("\nConexão ao MySQL foi encerrada")
    time.sleep(1)
    print("\nTeste de Conexão ao MySQL realizada com sucesso\n")
    time.sleep(2)