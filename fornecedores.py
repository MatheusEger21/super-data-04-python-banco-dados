from rich.console import Console
from rich.table import Table
from requests import get

from banco_dados import conectar


def consultar_fornecedores():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, cnpj, razao_social, nome_fantasia, cep, numero FROM fornecedores")
            registros = cursor.fetchall()

    tabela = Table(title="Fornecedores")
    tabela.add_column("Código")
    tabela.add_column("CNPJ")
    tabela.add_column("Razão Social")
    tabela.add_column("Nome Fantasia")
    tabela.add_column("CEP")
    tabela.add_column("Número")
    
    for fornecedor in registros:
        tabela.add_row(
            str(fornecedor[0]),
            str(fornecedor[1]),
            str(fornecedor[2]),
            str(fornecedor[3]),
            str(fornecedor[4]),
            str(fornecedor[5]),
        )

    console = Console()
    console.print(tabela)


def consultar_fornecedor_por_cnpj(cnpj:str):
    print("Consultando dados do fornecedor.....")
    resposta = get("https://api.opencnpj.org/" + cnpj)
    if resposta.status_code != 200:
        print("Não foi possivel consultar o CNPJ")
        return None, None, None, None
    else:
        dados = resposta.json()
        razao_social = dados["razao_social"]
        nome_fantasia = dados["nome_fantasia"]
        cep = dados["cep"]
        numero = dados["numero"]
        return razao_social, nome_fantasia, cep, numero


def cadastrar_fornecedor():
    cnpj = input("Digite o CNPJ: ")
    cnpj = formatar_cnpj(cnpj)
    if cnpj is None:
        return
    razao_social, nome_fantasia, cep, numero = consultar_fornecedor_por_cnpj(cnpj)
    if razao_social is None:
        return

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
            INSERT INTO fornecedores
            (cnpj, razao_social, nome_fantasia, cep, numero)
            VALUES(%s, %s, %s, %s, %s)
            """, (cnpj, razao_social, nome_fantasia, cep, numero))
            conexao.commit()
    print("Fornecedor cadastrado com sucesso")

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




# cadastrar_fornecedor()
consultar_fornecedores()