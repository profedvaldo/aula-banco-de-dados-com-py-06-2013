import mysql.connector

#vou conectar ao banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="edvaldotec_aula",
    password="!P^CH#8CnDYL",
    database="edvaldotec_produ"
)

#função para salvar no banco de dados
def inserir_produto():
  nome = input("Digite o nome do produto:")
  descricao = input("Descricao do produto:")
  valor = float(input("Digite o valor do produto:"))

  cursor = conexao.cursor()
  sql = "INSERT INTO produtos (nome_produto, descricao, valor) VALUES (%s, %s, %s)"
  valores = (nome, descricao, valor)
  cursor.execute(sql, valores)
  conexao.commit()
  print("SYS CerySoler - Salvo com sucesso!")

inserir_produto()
