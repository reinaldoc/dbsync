import sys
import cx_Oracle


class OracleDAO(object):
  def __init__(self):
    self.usuario = "admsrd"
    self.senha = "admsrd"
    self.bd = "10.13.1.1:1521/adm"
    self.conexao = cx_Oracle.connect(usuario+"/"+senha+"@"+bd)
    self.cursor = conexao.cursor()

  def list(self):
    self.cursor.execute("SELECT NOM, TELEFONE from vw_mat_servidores")
    self.resultado = cursor.fetchone()

    if resultado == None:
      print("Nenhum Resultado")
    else:
      while resultado:
        print(resultado[0])
        resultado = cursor.fetchone()

  def __del__(self):
    self.cursor.close()
    self.conexao.close()
