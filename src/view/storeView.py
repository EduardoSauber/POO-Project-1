class StoreView:
    def __init__(self, app):
        self._app = app

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
                finalized = True

    def list_products(self):
        products = self._app.get_all_products()
        for product in products:
            print(product)

    def add_to_user_cart(self,owner_id : str):
        finalized = False
        while finalized == False:
            print("--- Adicionar ao Carrinho ---")
            while True:
                print("Digite o código do produto (apenas letras e números, sem espaços):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação Cancelada.")
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
