########################################################################################################################
# import
from getpass import getpass

from src.controller.userController import UserManager
from src.controller.productController import ProductManager
from src.controller.cartController import CartManager

########################################################################################################################
# class
class AppManager:
    def __init__(self):
        self.user_manager = UserManager()
        self.product_manager = ProductManager()
        self.cart_manager = CartManager()

        self.user_manager.create_user("ADMIN","admin123","adminsupersecretid123","admin@mail","0",['admin'])

        self.personal_session_id = None

    def start(self):

        while True:
            if self.personal_session_id is None:
                print("Bem vindo!\nO que deseja realizar?\n")
                print("[ 1 ] - Log-in")
                print("[ 2 ] - Sign-in")
                print("[ 3 ] - Sair")
                opcao = input("Opção: ")

                match opcao:
                    case '1':
                        self.login()
                    case '2':
                        self.signin()
                    case '3':
                        print("Saindo do sistema.")
                        break
            else:
                user = self.user_manager.get_session_id_user(self.personal_session_id)
                if user.isAdmin():
                    self.admin_main_menu()
                else:
                    self.user_main_menu()



    # --- LOGIN E CADASTRO DE USUARIO ---
    def login(self):
        while self.personal_session_id is None:
            print("--- LOGIN ---")
            user_id = input("Digite seu CPF (digite 'sair' para sair): ")

            if user_id.lower() == "sair":
                print("Saindo do sistema.")
                break

            user_pswrd = getpass("Digite sua senha: ")

            check_session_id = self.user_manager.authenticate_user(user_id,user_pswrd)

            if check_session_id:
                self.personal_session_id = check_session_id
                print("Usuário logado com exito.")
            else:
                print("Acesso negado. Tente novamente.")

    def signin(self):
        pass

    # --- TELA INICIAL ---
    # -- cliente --
    def user_main_menu(self):
        pass

    # -- admin --
    def admin_main_menu(self):
        print("--- Painel de Administração ---")

        perms = self.user_manager.get_session_permissions(self.personal_session_id)

        print("[ 1 ] - Ver Catálogo de Produtos")
        print("[ 2 ] - Ver Relatório Diário")
        if 'cashier' in perms or 'admin' in perms:
            print("-- Operações de Caixa --")
            print("[ 2 ] - Processar Venda Física")
            print("[ 3 ] - [W.I.P]")
        if 'admin' in perms:
            print("-- Gerenciamento de Sistema --")
            print("[ 4 ] - Gerenciar Clientes")
            print("[ 5 ] - Gerenciar Estoque")

        opcao = input("Opção: ")
        match opcao:
            case '0':
                print("Fazendo logout.")
                self.user_manager.logout(self.personal_session_id)
                self.personal_session_id = None
                return
            case '2':
                pass
            case '3':
                pass
            case '4':
                if 'admin' in perms:
                    self.client_manager()
                else:
                    print("Opção inválida!")
            case '5':
                if 'admin' in perms:
                    self.stock_manager()
                else:
                    print("Opção inválida!")
            case _:
                print("Opção inválida!")

    def client_manager(self):
        pass

    def stock_manager(self):
        pass

# testbench
def testbench():
    testeApp = AppManager()
    testeApp.start()
if __name__ == '__main__':
    testbench()
