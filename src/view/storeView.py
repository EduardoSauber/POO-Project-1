from subprocess import call
import os
from time import sleep
class StoreView:
    def __init__(self, app):
        self._app = app

    def hold_menu(self,duration:int=5):
        print(f"O menu fechará em {duration} segundo(s)...")
        sleep(duration)
        call('clear' if os.name == 'posix' else 'cls')

    def create_product(self):
        finalized = False
        while finalized == False:
            print("--- CADASTRAR PRODUTO ---")
            print("Digite 'sair' para cancelar o cadastro.")

            name = None
            while True:
                print("Digite o nome do produto:")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt:
                    name = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            product_id = None
            while True:
                print("Digite o ID do produto (apenas letras e números, sem espaços):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt.isalnum():
                    product_id = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            price = None
            while True:
                print("Digite o preço do produto (use '.' para centavos):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt.replace(".", "").isnumeric():
                    price = float(inpt)
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            stock = None
            while True:
                print("Digite a quantidade inicial de estoque:")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt.isnumeric():
                    stock = int(inpt)
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            product = self._app.create_product([name, product_id, price, stock])
            if product:
                print("Produto cadastrado com sucesso!")
                self.hold_menu(3)
                finalized = True

    def edit_product(self):
        finalized = False
        while finalized == False:
            print("--- Editar Dados do Produto ---")
            product_id = None
            while True:
                print("Digite o ID do produto (apenas letras e números, sem espaços):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt.isalnum():
                    product_id = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            product = self._app.get_product(product_id)
            if not product:
                print("Produto não encontrado no sistema!")
                finalized = True
                return

            print(f"> {product}")

            print("[ 1 ] - Editar Nome")
            print("[ 2 ] - Editar Código")
            print("[ 3 ] - Editar Preço")
            print("[ 4 ] - Editar Estoque")
            print("[ 0 ] - Sair")
            opcao = input("Opção: ")
            match opcao:
                case '1':
                    n_name = self.edit_product_name()
                    if n_name:
                        self._app.edit_product_data(product_id, [None, n_name, None, None])
                    finalized = True
                case '2':
                    n_code = self.edit_product_code()
                    if n_code:
                        self._app.edit_product_data(product_id, [n_code, None, None, None])
                    finalized = True
                case '3':
                    n_price = self.edit_product_price()
                    if n_price:
                        self._app.edit_product_data(product_id, [None, None, n_price, None])
                    finalized = True
                case '4':
                    n_stock = self.edit_product_stock()
                    if n_stock:
                        self._app.edit_product_data(product_id, [None, None, None, n_stock])
                    finalized = True
                case '0':
                    aberto = False
                case _:
                    print("Opção inválida!")

    def edit_product_name(self):
        print("-- Editar nome do Produto --")
        print("Digite 'sair' para cancelar.")
        while True:
            print("Digite o novo nome do produto:")
            inpt = input().strip()
            if inpt.lower() == "sair":
                print("Operação cancelada.")
                return None
            if inpt:
                name = inpt
                return name
            else:
                print("Entrada inválida! Tente novamente.")

    def edit_product_code(self):
        print("-- Editar Código do Produto --")
        print("Digite 'sair' para cancelar.")
        while True:
            print("Digite o novo ID do produto (apenas letras e números, sem espaços):")
            inpt = input().strip()
            if inpt.lower() == "sair":
                print("Cadastro Cancelado.")
                return None
            if inpt.isalnum():
                product_id = inpt
                return product_id
            else:
                print("Entrada inválida! Tente novamente.")

    def edit_product_price(self):
        print("-- Editar Preço do Produto --")
        print("Digite 'sair' para cancelar.")
        while True:
            print("Digite o novo preço do produto (use '.' para centavos):")
            inpt = input().strip()
            if inpt.lower() == "sair":
                print("Cadastro Cancelado.")
                return None
            if inpt.replace(".", "").isnumeric():
                price = float(inpt)
                return price
            else:
                print("Entrada inválida! Tente novamente.")

    def edit_product_stock(self):
        print("-- Editar Estoque do Produto --")
        print("Digite 'sair' para cancelar.")
        while True:
            print("Digite a nova quantidade de estoque:")
            inpt = input().strip()
            if inpt.lower() == "sair":
                print("Cadastro Cancelado.")
                return None
            if inpt.isnumeric():
                stock = int(inpt)
                return stock
            else:
                print("Entrada inválida! Tente novamente.")

    def delete_product(self):
        finalized = False
        while finalized == False:
            print("--- Deletar Produto ---")
            while True:
                print("Digite o código do produto (apenas letras e números, sem espaços):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt.isalnum():
                    product_id = inpt
                    break
                else:
                    print("Entrada inválida. Tente novamente.")

            event = self._app.delete_product(product_id)

            if event:
                print("Produto removido do estoque com sucesso!")
                self.hold_menu(3)
                finalized = True
            else:
                print("Erro ao remover produto do estoque.")
                continue

    def list_products(self):
        products = self._app.get_all_products()
        print("--- Catálogo de Produtos ---")
        for product in products:
            print(product)
        self.hold_menu(10)

    def list_user_cart_products(self,owner_id:str):
        user_products = self._app.get_cart_products(owner_id)
        if not user_products:
            print("Não há produtos no carrinho!")
            return
        print("--- Seu Carrinho ---")
        total_price = 0
        for product in user_products:
            print(f"> {product['name']} (ID: {product['product_id']})")
            print(f"{product['quantity']} unidade(s) de R${product['unity_price']:.2f}")
            total_price += product['total_price']
            print("-"*20)
        print(f"Total: R${total_price:.2f}")
        self.hold_menu(10)

    def add_to_user_cart(self,owner_id : str):
        finalized = False
        while finalized == False:
            print("--- Adicionar ao Carrinho ---")
            while True:
                print("Digite o código do produto (apenas letras e números, sem espaços):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt.isalnum():
                    product_id = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            product = self._app.get_product(product_id)
            if not product:
                print(f"Produto '{product_id}' não existe no estoque!")
                continue

            print(f">> {product}")

            while True:
                print("Digite a quantidade desejada:")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação Cancelada.")
                    finalized = True
                    return
                if inpt.isnumeric() and int(inpt) > 0:
                    quantity = int(inpt)
                    if quantity > product.stock:
                        print(f"Apenas {product.stock} unidades em estoque!")
                        continue

                    event = self._app.add_to_user_cart([owner_id,product_id,quantity])

                    if event:
                        print("Produto adicionado ao carrinho!")
                        return
                    else:
                        print("Erro ao adicionar ao carrinho!")
                        return
                else:
                    print("Entrada inválida! Tente novamente.")

    def remove_from_user_cart(self,owner_id:str):
        finalized = False
        while finalized == False:
            print("--- Remover do Carrinho ---")
            while True:
                print("Digite o código do produto (apenas letras e números, sem espaços):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt.isalnum():
                    product_id = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            product = self._app.get_product(product_id)
            if not product:
                print(f"Produto '{product_id}' não existe no estoque!")
                continue

            print(f">> {product}")
            cart_quantity = self._app.get_cart_product_quantity(owner_id,product_id)

            if cart_quantity == 0:
                print(f"Produto {product_id} não está no seu carrinho.")
                finalized = True
                return

            if cart_quantity > 0:
                print(f"Quantidade no carrinho: {cart_quantity}")

            while True:
                print("Digite a quantidade que deseja remover:")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt.isnumeric():
                    rm_quantity = int(inpt)
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            if rm_quantity >= cart_quantity:
                event = self._app.remove_from_user_cart([owner_id,product_id])

            if rm_quantity < cart_quantity:
                event = self._app.add_to_user_cart([owner_id,product_id,-rm_quantity])

            if event:
                finalized = True
