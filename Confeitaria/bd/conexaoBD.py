import mysql.connector
import time


con = mysql.connector.connect(host='localhost',database='confeitaria',user='root',password='')
if con.is_connected():
    db_info = con.get_server_info()
    time.sleep(1)
    print("\nConectado ao servidor MySQL versão\n ",db_info)
    cursor = con.cursor()
    cursor.execute("\nselect * from  produtos;\n")
    linha = cursor.fetchall()
    time.sleep(1)
    print("\nConectado ao banco de dados\n ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    time.sleep(1)
    print("\nConexão ao MySQL foi encerrada\n")