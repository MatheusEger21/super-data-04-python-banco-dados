from mysql.connector import connect

def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="loja_db"
    )
    print("Conexão aberta com sucesso")
    return conexao

def consultar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, descricao FROM produtos")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Produtos:")
    for produto in registros:
        # print("id", produto[0], "\nNome:", produto[1], "\nDescrição:", produto[2], "\n\n")
        print(produto[0], " => ", produto[1], " => ", produto[2])
        

def cadastrar_produtos():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao) VALUES (%s, %s)",
        (nome, descricao)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto cadastrado com sucesso")


def apagar_produto():
    id_produto = int(input("Digite o id do produto para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto apagado com sucesso")


def editar_produto():
    id_produto = (int(input("Digite o id do produto para editar: ")))
    novo_nome = input("Digite o nome do produto: ")
    nova_descricao = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = %s, descricao = %s WHERE id = %s",
        (novo_nome, nova_descricao, id_produto)
    )  
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto alterado com sucesso")



def limpar_terminal():
    import os
    os.system("cls")

if __name__ == "__main__":
    menu = """MENU:
1   - Consultar produtos
2   - Cadastrar Produtos
3   - Apagar Produto
4   - Editar produto
99  - Sair

Digite o menu desejado: """

    menu_escolhido = int(input(menu))

    while menu_escolhido != 99:
        limpar_terminal()
        if menu_escolhido == 1:
            consultar_produtos()
        elif menu_escolhido == 2:
            cadastrar_produtos()
        elif menu_escolhido == 3:
            apagar_produto()
        elif menu_escolhido == 4:
            editar_produto()
        else:
            print("Opção Inválida")

        menu_escolhido = int(input(menu))