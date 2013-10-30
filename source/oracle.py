import sys
import cx_Oracle

usuario = "admsrd"
senha = "admsrd"
bd = "10.13.1.1:1521/adm"

conexao = cx_Oracle.connect(usuario+"/"+senha+"@"+bd)
cursor = conexao.cursor()

cursor.execute("SELECT * from vw_mat_servidores")
resultado = cursor.fetchone()

if resultado == None:
  print("Nenhum Resultado")
else:
  while resultado:
    print(resultado[0])
    resultado = cursor.fetchone()

cursor.close()
conexao.close()