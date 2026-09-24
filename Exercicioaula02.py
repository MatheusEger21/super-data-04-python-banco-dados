from mysql.connector import connect
from datetime import datetime

def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="helpdesk"
    )
    print("Conexão aberta com sucesso")
    return conexao


def cadastrar_categoria():
    nome = input("Nome da categoria: ")
    cor = input("Cor da categoria (HEX): ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO categorias (nome, cor) VALUES (%s, %s)", (nome, cor)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Categoria cadastrada com sucesso!")

def consultar_categoria():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, cor FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Categorias:")
    for categoria in categorias:
        print(categoria[0], " => ", categoria[1], " => ", categoria[2])


def cadastrar_tickets():
    numero_protocolo = str(input("Digite o número do protocolo: "))
    titulo = str(input("Digite o titulo para este ticket:"))
    descricao = str(input("Digite uma breve descrição para o ticket:"))
    status = str(input("Digite o status do chamado: [ABERTO, EM_ANALISE, RESOLVIDO, CANCELADO]: "))
    prioridade = str(input("Digite a prioridade do ticket [BAIXA, MEDIA, ALTA]: "))
    setor = str(input("Digite o setor que solicitou abertura do ticket [TI, RH, FINANCEIRO, ADMINISTRATIVO, MANUTENCAO]: "))
    descricao_solucao = str(input("Digite a descrição da solução: "))
    data_criacao = input("Digite da data de criação do ticket [ANO-MES-DIA]: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tickets (numero_protocolo, titulo, descricao, status, prioridade, setor, descricao_solucao, data_criacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (numero_protocolo, titulo, descricao, status, prioridade, setor, descricao_solucao, data_criacao)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto cadastrado com sucesso")


def consultar_tickets():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, numero_protocolo, titulo, descricao, status, prioridade, setor, descricao_solucao, data_criacao FROM tickets")
    tickets = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Tickets:")
    for ticket in tickets:
        print(ticket[1], " => ", ticket[2], " => ", ticket[3], " => ", ticket[7])


def apagar_tickets():
    id_ticket = int(input("Digite o id do ticket para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = %s", (id_ticket,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Ticket apagado com sucesso")


def editar_tickets():
    id_ticket = (int(input("Digite o id do ticket para editar: ")))
    novo_status = input("Digite o novo status do ticket [ABERTO, EM_ANALISE, RESOLVIDO, CANCELADO]:  ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE tickets SET status = %s WHERE id = %s",
        (novo_status, id_ticket)
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
1   - Cadastrar Ticket
2   - Consultar Ticket
3   - Editar Ticket
4   - Apagar Ticket
99  - Sair

Digite o menu desejado: """

    menu_escolhido = int(input(menu))

    while menu_escolhido != 99:
        limpar_terminal()
        if menu_escolhido == 1:
            cadastrar_tickets()
        elif menu_escolhido == 2:
            consultar_tickets()
        elif menu_escolhido == 3:
            editar_tickets()
        elif menu_escolhido == 4:
            apagar_tickets()
        else:
            print("Opção Inválida")

        menu_escolhido = int(input(menu))

    print("\n\nObrigado por usar nosso sistema!\n\n")
















# FEITO - Ex. 02: Criar um novo banco de dados chamado helpdesk:
# - Criar uma tabela de categorias com: nome, cor da categoria (hexadecimal) e id
#       Fazer o consultar categorias no python
#       Fazer o cadastro da categoria no python
# - Criar uma tabela de tickets com os seguintes campos:
# id int
# numero_protocolo: str
# titulo: str
# descricao: str
# status: str(ABERTO, EM_ANALISE, RESOLVIDO, CANCELADO)
# prioridade: str(BAIXA, MEDIA, ALTA)
# setor: (TI, RH, FINANCEIRO, ADMINISTRATIVO, MANUTENCAO)
# descricao_solucao: str
# data_criacao: datetime
# Fazer o CRUD em python para permitir interagir com a tabela de tickets