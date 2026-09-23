# Importa a função connect da biblioteca mysql.connector
# Ela será utilizada para criar a conexão com o banco MySQL
from mysql.connector import connect


# Cria uma função chamada conectar
# Essa função será responsável por abrir a conexão com o banco
def conectar():

    # Cria a conexão com o banco de dados
    conexao = connect(

        # Endereço onde o MySQL está instalado
        host="localhost",

        # Porta padrão utilizada pelo MySQL
        port=3306,

        # Usuário utilizado para acessar o banco
        user="root",

        # Senha do usuário do banco
        password="admin",

        # Nome do banco de dados que será utilizado
        database="loja_db"
    )

    print("Conexão aberta com sucesso")

    # Retorna a conexão para quem chamou a função
    return conexao


# ============================================================
# FUNÇÃO PARA CADASTRAR CLIENTE
# ============================================================

# Cria a função responsável pelo cadastro de clientes
def cadastrar_cliente():

    nome = input("Digite o nome do cliente: ")

    cnpj = input("Digite o CNPJ: ")
    cnpj = formatar_cnpj(cnpj)

    endereco = input("Digite o endereço: ")

    telefone = input("Digite o telefone: ")
    telefone = formatar_telefone(telefone)

    email = input("Digite o e-mail: ")

    limite_credito = float(input("Digite o limite de crédito: "))

    # Chama a função conectar()
    # Ela abre uma conexão entre Python e MySQL
    conexao = conectar()

    # Cria um cursor
    # O cursor é utilizado para executar comandos SQL
    cursor = conexao.cursor()


    # Cria o comando SQL que será executado
    # %s representa os valores que serão enviados posteriormente
    sql = """
        INSERT INTO clientes
        (nome, cnpj, endereco, telefone, email, limite_credito)
        VALUES (%s, %s, %s, %s, %s, %s)
    """


    # Cria uma tupla com os valores que serão enviados
    # para os %s da consulta SQL
    valores = (
        nome,
        cnpj,
        endereco,
        telefone,
        email,
        limite_credito
    )


    # Executa o comando SQL
    # O primeiro parâmetro é o SQL
    # O segundo parâmetro são os valores
    cursor.execute(sql, valores)


    # Confirma a alteração no banco de dados
    # Sem o commit(), o INSERT pode não ser gravado definitivamente
    conexao.commit()

    print("Cliente cadastrado com sucesso!")


    # Fecha o cursor
    cursor.close()

    # Fecha a conexão com o banco
    conexao.close()

def formatar_cnpj(cnpj):

    # Remove pontos, barras, hífens e espaços
    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    cnpj = cnpj.replace("-", "")
    cnpj = cnpj.replace(" ", "")

    # Verifica se possui exatamente 14 números
    if len(cnpj) != 14:
        print("CNPJ inválido!")
        return None

    # Monta o CNPJ no padrão
    cnpj_formatado = (
        cnpj[:2] + "." +
        cnpj[2:5] + "." +
        cnpj[5:8] + "/" +
        cnpj[8:12] + "-" +
        cnpj[12:14]
    )

    # Retorna o CNPJ formatado
    return cnpj_formatado

def formatar_telefone(telefone):

    # Remove espaços, parênteses e hífen
    telefone = telefone.replace(" ", "")
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace("-", "")

    # Verifica se possui 11 números
    if len(telefone) != 11:
        print("Telefone inválido!")
        return None

    # Monta o telefone no padrão
    telefone_formatado = (
        "(" + telefone[:2] + ") " +
        telefone[2:7] + "-" +
        telefone[7:11]
    )

    # Retorna o telefone formatado
    return telefone_formatado


# ============================================================
# FUNÇÃO PARA CONSULTAR CLIENTES
# ============================================================

# Cria a função responsável por consultar os clientes
def consultar_clientes():

    conexao = conectar()

    cursor = conexao.cursor()

    # Cria o comando SQL para buscar os clientes
    sql = """
        SELECT
            id,
            nome,
            cnpj,
            endereco,
            telefone,
            email,
            limite_credito
        FROM clientes
    """


    # Executa o comando SELECT
    cursor.execute(sql)

    # Pega todos os registros encontrados pelo SELECT
    # fetchall() retorna todos os resultados
    clientes = cursor.fetchall()

    # Mostra um título no terminal
    print("\n========== CLIENTES ==========")

    # Percorre todos os clientes encontrados
    # Cada cliente será armazenado temporariamente na variável cliente
    for cliente in clientes:

        # Mostra o ID do cliente
        # cliente[0] representa a primeira coluna do SELECT
        print("ID:", cliente[0])

        # Mostra o nome
        # cliente[1] representa a segunda coluna
        print("Nome:", cliente[1])

        # Mostra o CNPJ
        # cliente[2] representa a terceira coluna
        print("CNPJ:", cliente[2])

        # Mostra o endereço
        # cliente[3] representa a quarta coluna
        print("Endereço:", cliente[3])

        # Mostra o telefone
        # cliente[4] representa a quinta coluna
        print("Telefone:", cliente[4])

        # Mostra o e-mail
        # cliente[5] representa a sexta coluna
        print("E-mail:", cliente[5])

        # Mostra o limite de crédito
        # cliente[6] representa a sétima coluna
        print("Limite de crédito:", cliente[6])

        # Cria uma linha para separar um cliente do outro
        print("-----------------------------")


    # Fecha o cursor
    cursor.close()

    # Fecha a conexão com o banco
    conexao.close()


# ============================================================
# FUNÇÃO PARA EDITAR CLIENTE
# ============================================================

# Cria a função responsável por editar um cliente
def editar_cliente():

    # Pede o ID do cliente que será alterado
    # int() transforma o valor digitado em número inteiro
    id_cliente = int(input("Digite o ID do cliente que deseja editar: "))


    # Pede o novo nome
    nome = input("Digite o novo nome: ")

    # Pede o novo CNPJ
    cnpj = input("Digite o novo CNPJ: ")

    # Pede o novo endereço
    endereco = input("Digite o novo endereço: ")

    # Pede o novo telefone
    telefone = input("Digite o novo telefone: ")

    # Pede o novo e-mail
    email = input("Digite o novo e-mail: ")

    # Pede o novo limite de crédito
    # float() transforma o texto digitado em número decimal
    limite_credito = float(
        input("Digite o novo limite de crédito: ")
    )


    # Abre a conexão com o banco
    conexao = conectar()

    # Cria o cursor
    cursor = conexao.cursor()


    # Cria o comando SQL para atualizar o cliente
    sql = """
        UPDATE clientes
        SET
            nome = %s,
            cnpj = %s,
            endereco = %s,
            telefone = %s,
            email = %s,
            limite_credito = %s
        WHERE id = %s
    """


    # Cria uma tupla com os valores que serão enviados
    # para cada %s do comando SQL
    valores = (
        nome,
        cnpj,
        endereco,
        telefone,
        email,
        limite_credito,
        id_cliente
    )


    # Executa o comando UPDATE
    cursor.execute(sql, valores)


    # Confirma a alteração no banco
    conexao.commit()


    # Verifica se algum registro foi alterado
    # rowcount informa quantas linhas foram afetadas
    if cursor.rowcount > 0:

        # Se foi alterado pelo menos um registro
        print("Cliente atualizado com sucesso!")

    else:

        # Se nenhum registro foi encontrado com aquele ID
        print("Cliente não encontrado.")


    # Fecha o cursor
    cursor.close()

    # Fecha a conexão
    conexao.close()


# ============================================================
# FUNÇÃO PARA APAGAR CLIENTE
# ============================================================

# Cria a função responsável por excluir um cliente
def apagar_cliente():

    # Pede o ID do cliente que será excluído
    # int() transforma o valor digitado em número inteiro
    id_cliente = int(
        input("Digite o ID do cliente que deseja apagar: ")
    )


    # Abre uma conexão com o banco
    conexao = conectar()

    # Cria um cursor para executar o SQL
    cursor = conexao.cursor()


    # Cria o comando SQL para excluir o cliente
    sql = """
        DELETE FROM clientes
        WHERE id = %s
    """


    # Executa o DELETE
    # (id_cliente,) é uma tupla com apenas um valor
    cursor.execute(sql, (id_cliente,))


    # Confirma a exclusão no banco
    conexao.commit()


    # Verifica se algum registro foi excluído
    if cursor.rowcount > 0:

        # Se encontrou e excluiu o cliente
        print("Cliente apagado com sucesso!")

    else:

        # Se não encontrou nenhum cliente com aquele ID
        print("Cliente não encontrado.")


    # Fecha o cursor
    cursor.close()

    # Fecha a conexão
    conexao.close()


# ============================================================
# MENU PRINCIPAL
# ============================================================

# Cria a função que controla o menu principal
def menu():

    # while True cria um loop infinito
    # O menu continuará aparecendo até o usuário escolher 0
    while True:

        print("\n========== MENU ==========")

        print("1 - Cadastrar cliente")

        print("2 - Consultar clientes")

        print("3 - Editar cliente")

        print("4 - Apagar cliente")

        print("0 - Sair")


        opcao = input("Digite uma opção: ")


        if opcao == "1":

            # Chama a função de cadastrar cliente
            cadastrar_cliente()


        # Verifica se o usuário escolheu 2
        elif opcao == "2":

            # Chama a função de consultar clientes
            consultar_clientes()


        # Verifica se o usuário escolheu 3
        elif opcao == "3":

            # Chama a função de editar cliente
            editar_cliente()


        # Verifica se o usuário escolheu 4
        elif opcao == "4":

            # Chama a função de apagar cliente
            apagar_cliente()


        # Verifica se o usuário escolheu 0
        elif opcao == "0":

            # Mostra mensagem de encerramento
            print("Programa encerrado.")

            # break interrompe o while True
            break


        # Se não for nenhuma das opções anteriores
        else:

            # Informa que a opção não existe
            print("Opção inválida.")


# ============================================================
# INICIAR O PROGRAMA
# ============================================================

# Chama a função menu()
# Isso faz o programa começar pelo menu principal
menu()