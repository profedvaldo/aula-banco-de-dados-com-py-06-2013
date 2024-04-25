import mysql.connector

# Estabelecendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="edvaldotec_aula",
    password="!P^CH#8CnDYL",
    database="edvaldotec_produ"
)

# Função para inserir um novo produto no banco de dados
def inserir_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    valor = float(input("Digite o valor do produto: "))

    cursor = conexao.cursor()
    sql = "INSERT INTO produtos (nome_produto, descricao, valor) VALUES (%s, %s, %s)"
    valores = (nome, descricao, valor)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Produto inserido com sucesso!")

# Função para pesquisar produtos por nome
def pesquisar_produtos_por_nome():
    nome = input("Digite o nome do produto a ser pesquisado: ")

    cursor = conexao.cursor()
    sql = "SELECT * FROM produtos WHERE nome_produto LIKE %s"
    valor_pesquisa = "%" + nome + "%"
    cursor.execute(sql, (valor_pesquisa,))
    resultados = cursor.fetchall()
    if resultados:
        for produto in resultados:
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Descrição: {produto[2]}")
            print(f"Valor: R${produto[3]}")
            print("-------------------------")
    else:
        print("Nenhum produto encontrado.")

# Perguntar ao usuário se deseja inserir ou consultar dados
opcao = input("Escolha uma opção:\n1. Inserir um produto\n2. Pesquisar produtos por nome\nOpção: ")

# Executar a ação selecionada
if opcao == "1":
    inserir_produto()
elif opcao == "2":
    pesquisar_produtos_por_nome()
else:
    print("Opção inválida. Encerrando o programa.")
