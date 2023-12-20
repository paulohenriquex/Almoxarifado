import uuid
import datetime


def cadastrarProduto(produtos):
    id = uuid.uuid4()
    status = True
    print("")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    totalvendas = 0
    dataCadastro = datetime.datetime.now()
    dataVenda = ""
    produtos.append(
        {"id": id, "nome": nome, "quantidade": quantidade, "preco": preco, "status": status, "totalvendas": totalvendas, "datacadastro": dataCadastro,    "dataVenda": dataVenda})
    print("")


def mostrarProdutos(produtos):
    print("1 - Produtos em estoque")
    print("2 - Produtos fora de estoque")
    print("3 - Todos os produtos")
    print("")
    opcao = int(input("Digite a opção desejada: "))
    print("")
    if opcao == 1:
        print("")
        print("Produtos em estoque")
        print("")
        for produto in produtos:
            if produto["status"] == True and produto["quantidade"] > 0:
                print("ID: ", produto["id"])
                print("Nome: ", produto["nome"])
                print("Quantidade: ", produto["quantidade"])
                # Correção: Formate o preço com duas casas decimais
                print(f"Preço: R$ {produto['preco']:.2f}")
                print("")
        else:
            print("Produto não encontrado ou com estoque zerado.")
            print("")
    elif opcao == 2:
        print("")
        print("Produtos fora de estoque")
        print("")
        for produto in produtos:
            if produto["status"] == False:
                print("ID: ", produto["id"])
                print("Nome: ", produto["nome"])
                print("Quantidade: ", produto["quantidade"])
                # Correção: Formate o preço com duas casas decimais
                print(f"Preço: R$ {produto['preco']:.2f}")
                print("")
            else:
                print("Produto não encontrado ou com estoque zerado.")
                print("")
    elif opcao == 3:
        print("")
        print("Todos os produtos")
        print("")
        for produto in produtos:
            print("ID: ", produto["id"])
            print("Nome: ", produto["nome"])
            print("Quantidade: ", produto["quantidade"])
            # Correção: Formate o preço com duas casas decimais
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("")


def alterarProduto(produtos):
    busca = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"] == busca:
            print("Produto encontrado")
            print("")
            nome = input("Digite o novo nome: ")
            quantidade = int(input("Digite a nova quantidade: "))
            preco = float(input("Digite o novo preço: "))
            produto["ID"] = id
            produto["nome"] = nome
            produto["quantidade"] = quantidade
            produto["preco"] = preco
            produto["status"] = True
            print("Produto alterado com sucesso")


def excluirProduto(produtos):
    busca = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"] == busca and produto["status"]:
            print("Produto encontrado")
            produto["status"] = False
            produto["quantidade"] = 0
            print("Produto excluído com sucesso")
            print("")
            return
    else:
        print("Produto não encontrado")


def realizarVenda(produtos):
    busca = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"] == busca and produto["status"]:
            print("Produto encontrado")
            print("")
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade > produto["quantidade"]:
                print("Quantidade indisponível")
                print("")
                return
            else:
                produto["quantidade"] -= quantidade
                print("Venda realizada com sucesso")
                produto["totalvendas"] += quantidade*produto["preco"]
                print("")
                if produto["quantidade"] == 0:
                    produto["status"] = False
                    produto["dataVenda"] = datetime.datetime.now()
                return
        else:
            print("Produto não encontrado ou com estoque zerado")
            print("")


def relatorioVendas(produtos):
    total = 0
    print("Produtos vendidos")
    print("")
    for produto in produtos:
        print("ID: ", produto["id"])
        print("Nome: ", produto["nome"])
        print("Quantidade: ", produto["quantidade"])
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("Total de vendas: ", produto["totalvendas"])
        print("")


def main():
    produtos = []
    while True:
        print("")
        print("===== Controle de Estoque =====")
        print("1 - Cadastrar Produto")
        print("2 - Mostrar Estoque")
        print("3 - Alterar Produto")
        print("4 - Excluir Produto")
        print("5 - Realizar Venda")
        print("6 - Relatório de Vendas")
        print("7 - Sair")
        print("")
        print("Teste do git e oneDrive.")
        print("Segundo teste")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrarProduto(produtos)
        elif opcao == 2:
            mostrarProdutos(produtos)
        elif opcao == 3:
            alterarProduto(produtos)
        elif opcao == 4:
            excluirProduto(produtos)
        elif opcao == 5:
            realizarVenda(produtos)
        elif opcao == 6:
            relatorioVendas(produtos)
        elif opcao == 7:
            print("Saindo...")
            break
        else:
            print("Opção Inválida")


if __name__ == "__main__":
    main()
