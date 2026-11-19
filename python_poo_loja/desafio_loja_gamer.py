class Produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def exibir_mensagem(self):

        print(f'{self.nome}: R${self.preco:,.2f}\n'
              f'Quantidade: {self.quantidade}\n'
              f'Categoria: {self.categoria}'
        )

    def adicionar_estoque(self, quantidade_adicionada):
        if type(quantidade_adicionada) is not int:
            print("Quantidade adicionada deve ser um inteiro")
            return False

        if quantidade_adicionada <= 0:
            print("Quantidade adicionada é inválida")
            return False

        self.quantidade += quantidade_adicionada

        return True

    def remover_estoque(self, quantidade_removida):
        if type(quantidade_removida) is not int:
            print("Quantidade removida deve ser um inteiro")
            return False
    
        if quantidade_removida <= 0:
            print("Quantidade removida é inválida")
            return False

        if self.quantidade < quantidade_removida:
            print("Estoque insuficiente")
            return False

        self.quantidade -= quantidade_removida

        return True

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco_atual):
        if isinstance(preco_atual, bool):
            raise TypeError("Tipo de valor inválido")       

        if not isinstance(preco_atual, (int, float)):
            raise TypeError("Tipo de valor inválido")    
            
        if preco_atual <= 0:
            raise ValueError("Valor Inválido")

        self.__preco = preco_atual

        
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade_atual):
        if isinstance(quantidade_atual, bool):
            raise TypeError("Tipo de valor inválido")
        
        if not isinstance(quantidade_atual, int):
            raise TypeError("Tipo de valor inválido")

        if quantidade_atual < 0:
            raise ValueError("Quantidade Inválida")

        self.__quantidade = quantidade_atual

class Controle(Produto):
    def __init__(self, nome, preco, quantidade, categoria, plataforma):
        super().__init__(nome, preco, quantidade, categoria)
        self.plataforma = plataforma

    def exibir_mensagem(self):
        super().exibir_mensagem()
        print(f'Plataforma: {self.plataforma}')

class Teclado(Produto):
    def __init__(self, nome, preco, quantidade, categoria, tipo_switch):
        super().__init__(nome, preco, quantidade, categoria)
        self.tipo_switch = tipo_switch

    def exibir_mensagem(self):
        super().exibir_mensagem()
        print(f'Tipo de Switch: {self.tipo_switch}')


class Estoque():
    def __init__(self):
        self.lista_produtos = []
        self.historico_vendas = []

    def listar_produto(self):
        for item in self.lista_produtos:
            item.exibir_mensagem()
            print("---------------")

    def buscar_produto(self, nome):
        for item in self.lista_produtos:
            if item.nome.strip().lower() == nome.strip().lower():
                return item

        print("Nenhum produto encontrado! ")    
        return None
    
    def adicionar_produto(self, produto):        
        for item in self.lista_produtos:
            if item.nome.strip().lower() == produto.nome.strip().lower():
                print("O produto já está cadastrado!")
                return False
            
        self.lista_produtos.append(produto)
        return True

    def remover_produto(self, produto):
        for item in self.lista_produtos:
            if item.nome == produto:
                self.lista_produtos.remove(item)
                return True
        
        print("Produto não existe!")
        return False
        
    def quantidade_total(self):
        total = 0

        for item in self.lista_produtos:
            total += item.quantidade

        return total
        
    def valor_total_estoque(self):
        soma_total = 0

        for item in self.lista_produtos:
            soma_total += item.preco * item.quantidade

        return soma_total

    def vender_produto(self, nome, quantidade, cliente):
        produto = self.buscar_produto(nome)

        if produto is None:
            return False

        if produto.remover_estoque(quantidade):
            venda = Venda(produto, quantidade, cliente)
            self.historico_vendas.append(venda)
            print("Produto foi vendido!")
            return True
        else:
            return False

    def cancelar_compra(self, indice):
        if type(indice) is not int:
            return False
        
        if indice < 0 or indice >= len(self.historico_vendas):
            return False

        venda_cancelada = self.historico_vendas[indice]
        quantidade_estornada = venda_cancelada.quantidade

        if not venda_cancelada.produto.adicionar_estoque(quantidade_estornada):
            print("Não foi possivel realizar o cancelamento da compra")
            return False

        del self.historico_vendas[indice]
        return True

    def listar_historico_vendas(self):
        for indice, item in enumerate(self.historico_vendas):
            print(f"Venda N°: {indice}")
            print(f"Cliente: {item.cliente.nome}")
            print(f"Produto: {item.nome_produto}")
            print(f"Preço Unitário: R${item.preco_unitario:.2f}")
            print(f"Quantidade: {item.quantidade}")
            print(f"Total: R${item.valor_total:.2f}")
            print("-----------------------------")

    def listar_compras_cliente(self, cpf):
        encontrou = False

        for item in self.historico_vendas:
            if item.cliente.cpf == cpf:
                print(f'Produto: {item.nome_produto}')
                print(f'Quantidade Comprada: {item.quantidade}')
                print(f'Valor Total: {item.valor_total}\n')
                encontrou = True

        if not encontrou:
            print("Cliente não possui compras")

        return encontrou

    def total_gastos_cliente(self, cpf):
        total = 0

        for item in self.historico_vendas:
            if item.cliente.cpf == cpf:
                total += item.valor_total

        return total

    def faturamento_total(self):
        total = 0
        
        for item in self.historico_vendas:
            total += item.valor_total

        return total
            

class Venda:
    def __init__(self, produto, quantidade, cliente):
        self.produto = produto
        self.quantidade = quantidade
        self.cliente = cliente

        self.nome_produto = produto.nome
        self.preco_unitario = produto.preco
        self.valor_total = self.preco_unitario * self.quantidade


class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

def normalizar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    if not cpf:
        raise ValueError("CPF não pode ficar vazio.")
    
    if not cpf.isdigit():
        raise ValueError("CPF deve conter apenas números.")    
    
    if len(cpf) != 11:
        raise ValueError("CPF deve possuir 11 dígitos.")

    return cpf

def exibir_informacoes_cliente(cliente):
    print(f"Cliente: {cliente.nome}")
    print(f"CPF: {cliente.cpf}")
    print(f"E-mail: {cliente.email}\n")

def formatar_moeda(valor):
    valor_formatado = f"{valor:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")

    return valor_formatado

def menu():
    print("""\n
================================
          LOJA GAMER
================================

[1]\tCadastrar Produto
[2]\tListar Produtos
[3]\tBuscar Produto
[4]\tAdicionar Produto ao Estoque
[5]\tRemover Produto do Estoque
[6]\tCadastrar Cliente
[7]\tListar Cliente
[8]\tRealizar Venda
[9]\tHistórico de Vendas 
[10]\tCompras por Cliente
[11]\tTotal Gasto por Cliente
[12]\tCancelar Venda
[13]\tFaturamento Total
[14]\tValor Total do Estoque

[0]\tSair
""" )
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao < 0 or opcao > 14:
                raise ValueError("A opção escolhida deve ser uma das apresentadas no menu")

            return opcao

        except ValueError:
            print("Entrada inválida! Digite uma opção entre 0 e 14.")

estoque = Estoque()
lista_clientes = []        

escolha = menu()

while escolha != 0:
    if escolha == 1:
        while True:
            try:
                nome_produto = input("Nome do Produto: ")
                if not nome_produto.strip():
                    raise ValueError("Nome do produto não pode ficar vazio")
                
                preco = float(input("Preço do Produto: "))

                quantidade = int(input("Quantidade do Produto: "))
                
                categoria = input("Qual a categoria do Produto: [Controle/Teclado/Outro]: ")
                categoria_normal = categoria.strip().lower()

                if not categoria_normal:
                    raise ValueError("Categoria não pode ficar vazia")

                if categoria_normal == "controle":
                    plataforma = input("Qual a plataforma compativel com esse controle: ")
                    if not plataforma.strip():
                        raise ValueError("Plataforma não pode ficar vazia")
                    produto = Controle(nome_produto, preco, quantidade, categoria, plataforma)

                elif categoria_normal == "teclado":
                    tipo_switch = input("Qual o tipo de switch do teclado: ")
                    if not tipo_switch.strip():
                        raise ValueError("Tipo de switch não pode ficar vazio")

                    produto = Teclado(nome_produto, preco, quantidade, categoria, tipo_switch)

                else:
                    produto = Produto(nome_produto, preco, quantidade, categoria)

                operacao = estoque.adicionar_produto(produto)

                if operacao:
                    print("Estoque atualizado com sucesso!")
                else:
                    print("Não foi possível atualizar o estoque.")
                break
            
            except (ValueError, TypeError):
                print("Algum dos valores inseridos são inválidos")
                break

    elif escolha == 2:
        if not estoque.lista_produtos:
            print("Estoque não possui nem um produto cadastrado ainda! ")
        else:
            estoque.listar_produto()

    elif escolha == 3:
        produto_procurado = input("Informe o produto que procura: ")
        produto = estoque.buscar_produto(produto_procurado)

        if produto is None:
            print("Produto não encontrado no estoque!")
        else:
            produto.exibir_mensagem()

    elif escolha == 4:
        while True:
            try:
                produto_adicionado = input("Informe o nome do produto que deseja adicionar ao estoque: ")
                if not produto_adicionado.strip():
                    raise ValueError("É necessário informar o nome do produto")
                
                produto = estoque.buscar_produto(produto_adicionado)

                if produto is None:
                    print("Produto não cadastrado no estoque!")
                    continue
                
                quantidade_adicionada = int(input("Informe a quantidade que deseja adicionar ao estoque: "))
                operacao = produto.adicionar_estoque(quantidade_adicionada)

                if operacao:
                    print("Estoque atualizado com sucesso!")
                else:
                    print("Não foi possível atualizar o estoque.")
                break

            except ValueError as error:
                print(f"Erro: {error}")

    elif escolha == 5:
        while True:
            try:
                produto_removido = input("Informe o produto que deseja remover do estoque: ")
                if not produto_removido.strip():
                    raise ValueError("É necessário informar o nome do produto")

                produto = estoque.buscar_produto(produto_removido)

                if produto is None:
                    print("Produto não cadastrado no estoque!")
                    continue

                quantidade_removida = int(input("Informe a quantidade que deseja remover: "))
                operacao = produto.remover_estoque(quantidade_removida)

                if operacao:
                    print("Estoque atualizado com sucesso!")
                else:
                    print("Não foi possível atualizar o estoque.")
                break

            except ValueError as error:
                print(f"Erro: {error}")

    elif escolha == 6:
        while True:
            try:
                nome_cliente = input("Digite o nome do cliente: ")
                if not nome_cliente.strip():
                    raise ValueError("Nome do cliente não pode ficar vazio.")
                
                cpf = input("Digite o cpf do cliente: ")
                cpf = normalizar_cpf(cpf)
                
                email = input("Insira o email do cliente: ")
                if not email.strip():
                    raise ValueError("E-mail não pode ficar vazio.")

                cliente = Cliente(nome_cliente, cpf, email)

                for item in lista_clientes:
                    if item.cpf == cpf:
                        print("Cliente já cadastrado no sistema!")
                        break

                else:
                    lista_clientes.append(cliente)
                    print("Cliente cadastrado com sucesso!")
                    break
 
            except ValueError as error:
                print(f"Erro: {error}")
                break

    elif escolha == 7:
        if not lista_clientes:
            print("A lista de clientes esta vazia!")
        else:
            for item in lista_clientes:
                exibir_informacoes_cliente(item)   

    elif escolha == 8:
        while True:
            try:
                if not estoque.lista_produtos:
                    print("Estoque não possui nem um produto cadastrado ainda! ")
                    break

                if not lista_clientes:
                    print("A lista de clientes esta vazia!")
                    break

                cliente_cpf = input("Digite o CPF do cliente: ")
                cpf = normalizar_cpf(cliente_cpf)

                cliente = None
                for item in lista_clientes:
                    if item.cpf == cpf:
                        cliente = item
                        break

                if cliente is None:
                    print("Cliente não encontrado!")
                    break

                nome_produto = input("Nome do Produto: ")
                if not nome_produto.strip():
                    raise ValueError("Nome do produto não pode ficar vazio")

                quantidade_vendida = int(input("Quantidade Vendida: "))
                if quantidade_vendida <= 0:
                    raise ValueError("A quantidade deve ser maior que zero.")
                
                operacao = estoque.vender_produto(nome_produto, quantidade_vendida, cliente)

                if operacao:
                    print("Venda realizada com sucesso!")
                else:
                    print("Não foi possível realizar A venda.")
                break

            except ValueError as error:
                print(f"Erro: {error}")

    elif escolha == 9:
        if not estoque.historico_vendas:
            print("Não houve nenhuma venda!")
        else:
            estoque.listar_historico_vendas()

    elif escolha == 10:
        try:
            if not estoque.historico_vendas:
                print("Não foram realizadas vendas!")
            else: 
                cpf = input("Digite o cpf do cliente:\n ")
                cpf = normalizar_cpf(cpf)
                cliente_tem_compras = estoque.listar_compras_cliente(cpf)

                if cliente_tem_compras:
                    print("Cliente tem um historico de compras no sistema! ")

        except ValueError as error:
            print(f"Erro: {error}")

    elif escolha == 11:
        try:
            if not estoque.historico_vendas:
                print("Não foram realizadas vendas para esse cliente!")
            else:
                cpf = input("Digite o cpf do cliente: ")
                cpf = normalizar_cpf(cpf)

                total = estoque.total_gastos_cliente(cpf)
                valor_formatado = formatar_moeda(total) 

                if total == 0:
                    print("Cliente não possui compras registradas.")
                else:
                    print(f"O total gasto pelo cliente foi: R${valor_formatado}")

        except ValueError as error:
            print(f"Erro: {error}")

    elif escolha == 12:
        try: 
            if not estoque.historico_vendas:
                print("Não houve nenhuma venda!")
            else:            
                estoque.listar_historico_vendas()

                indice = int(input("Qual a posição da venda que deseja cancelar: "))
                compra_cancelada = estoque.cancelar_compra(indice)

                if compra_cancelada:
                    print("A compra foi cancelada com sucesso!")
                else:
                    print("Infelizmente não foi possível cancelar sua compra!")

        except ValueError as error:
            print(f"Erro: {error}")

    elif escolha == 13:
        if not estoque.historico_vendas:
            print("Não houve nenhuma venda!")
        else:
            faturamento_total = estoque.faturamento_total()
            valor_formatado = formatar_moeda(faturamento_total)

            print(f"O faturamento total é: R${valor_formatado}")

    elif escolha == 14:
        if not estoque.lista_produtos:
            print("Estoque não possui nem um produto cadastrado ainda! ")
        else:
            valor_total_estoque = estoque.valor_total_estoque()
            valor_formatado = formatar_moeda(valor_total_estoque)

            print(f"O valor total do estoque é: R${valor_formatado}")

    escolha = menu()

print("Encerrando a Loja Gamer...")