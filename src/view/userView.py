from subprocess import call
import os
from time import sleep

class UserView:
    def __init__(self,app,storeview_instance):
        self._app = app
        self._store_view = storeview_instance

    def hold_menu(self,duration:int=5,text:bool=True):
        if text:
            print(f"O menu fechará em {duration} segundo(s)...")
        sleep(duration)
        call('clear' if os.name == 'posix' else 'cls')

    def main_menu(self):
        self.hold_menu(0,False)
        print("--- Painel de Usuário ---")
        print(f"Bem vindo, {self._app.get_user_username(self._app.personal_session_id)}!")
        print("-- Menu --")
        print("[ 1 ] - Ver Catálogo de Produtos")
        print("[ 2 ] - Listar Produtos do Carrinho")
        print("[ 3 ] - Adicionar ao Carrinho")
        print("[ 4 ] - Remover do Carrinho")
        print("[ 5 ] - Finalizar Venda")
        print("[ 0 ] - Sair")

        opcao = input("Opção: ")
        match opcao:
            case '1':
                self.hold_menu(0,False)
                self.products_catalog()
            case '2':
                self.hold_menu(0,False)
                self.list_cart()
            case '3':
                self.hold_menu(0,False)
                self.add_to_cart()
            case '4':
                self.hold_menu(0,False)
                self.remove_from_cart()
            case '5':
                self.hold_menu(0,False)
                self.finish_sale()
            case '0':
                return "LOGOUT"
            case _:
                print("Opção inválida!")

    def products_catalog(self):
        self._store_view.list_products()

    def list_cart(self):
        self._store_view.list_user_cart_products(self._app.get_user_by_sessionid(self._app.personal_session_id).cpf)

    def add_to_cart(self):
        self._store_view.add_to_user_cart(self._app.get_user_by_sessionid(self._app.personal_session_id).cpf)

    def remove_from_cart(self):
        self._store_view.remove_from_user_cart(self._app.get_user_by_sessionid(self._app.personal_session_id).cpf)

    def finish_sale(self):
        self._store_view.finalize_purchase(self._app.get_user_by_sessionid(self._app.personal_session_id).cpf)