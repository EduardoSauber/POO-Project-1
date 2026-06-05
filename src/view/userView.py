class UserView:
    def __init__(self,app,storeview_instance):
        self._app = app
        self._store_view = storeview_instance

    def main_menu(self):
        print("--- Painel de Usuário ---")

        print("[ 1 ] - Ver Catálogo de Produtos")
        print("[ 2 ] - Adicionar ao Carrinho")
        print("[ 3 ] - Remover do Carrinho")
        print("[ 4 ] - Finalizar Venda")
        print("[ 0 ] - Sair")

        opcao = input("Opção: ")
        match opcao:
            case '1':
                self.products_catalog()
            case '2':
                self.add_to_cart()
            case '3':
                self.remove_from_cart()
            case '4':
                self.finish_sale()
            case '0':
                return "LOGOUT"
            case _:
                print("Opção inválida!")

    def products_catalog(self):
        self._store_view.list_products()

    def add_to_cart(self):
        self._store_view.add_to_user_cart(self._app.get_user_by_sessionid(self._app.personal_session_id).cpf)

    def remove_from_cart(self):
        # storeView cuida dessa parte
        pass

    def finish_sale(self):
        # storeView cuida dessa parte
        pass