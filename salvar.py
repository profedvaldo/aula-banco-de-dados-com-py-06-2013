import mysql.connector

#Aqui estou ligando a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="edvaldo.tec.br",
    user="edvaldotec_aula",
    password="!P^CH#8CnDYL",
    database="edvaldotec_produ"
)

#função para inserir um novo produto no banco de dados
def inserir_produto():
  nome=input("Digite o nome do produto:")
  descricao=input("Digite a descricao:")
  valor=float(input("Digite o valor do produto"))
  
  cursor=conexao.cursor()
  sql="INSERT INTO produtos (nome_produto, descricao, valor) VALUES (%s, %s, %s)"
  valores=(nome,descricao,valor)
  cursor.execute(sql, valores)
  conexao.commit()
  print("Produto Inserido com Sucesso - Miguelito System")

inserir_produto()
