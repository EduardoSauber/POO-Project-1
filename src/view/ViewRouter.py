import getpass

from src.controller.appController import AppManager

class Terminal_View:
    def __init__(self):
        self._app_controller = AppManager()

    @property
    def personal_session_id(self):
        return self._app_controller.personal_session_id

    def start(self):
        while True:
            if self.personal_session_id is None:
                print("Bem vindo!\nO que deseja realizar?\n")
                print("[ 1 ] - Log-in")
                print("[ 2 ] - Sign-in")
                print("[ 0 ] - Sair")
                opcao = input("Opção: ")

                match opcao:
                    case '1':
                        self.login_page()
                    case '2':
                        self.signin_page()
                    case '0':
                        print("Saindo do sistema.")
                        break
                    case _:
                        print("Opção inválida!")
            else:
                #user = self._user_manager.get_session_id_user(self.personal_session_id)
                user = self._app_controller.is_user_admin
                if user:
                    self.admin_main_menu()
                else:
                    self.user_main_menu()

    def login_page(self):
        while self.personal_session_id is None:
            print("--- LOGAR ---")
            try:
                user_id = input("Digite seu CPF: ")
                user_password = getpass.getpass("Digite sua senha: ")
                self._app_controller.login(user_id, user_password)
            except ValueError as error:
                print(f"Erro: {error}. Tente novamente.")

    def signin_page(self):
        while self.personal_session_id is None:
            print("--- CADASTRAR-SE ---")
            try:
                pass
            except ValueError as error:
                print(f"Erro: {error}. Tente novamente.")


    def user_main_menu(self):
        print("LOGOU")

    def admin_main_menu(self):
        print("--- Painel de Administração ---")

        perms = [] #self._user_manager.get_session_permissions(self.personal_session_id)

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
        print("-- Sistema --")
        print("[ 0 ] - Sair")

        opcao = input("Opção: ")
        match opcao:
            case '0':
                print("Fazendo logout.")
                #self._user_manager.logout(self.personal_session_id)
                #self.personal_session_id = None
                return
            case '2':
                pass
            case '3':
                pass
            case '4':
                if 'admin' in perms:
                    pass
                    #self.client_manager()
                else:
                    print("Opção inválida!")
            case '5':
                if 'admin' in perms:
                    pass
                    #self.stock_manager()
                else:
                    print("Opção inválida!")
            case _:
                print("Opção inválida!")

# testbench
def testbench():
    print("Rodando modo teste:")
    app = Terminal_View()
    app.start()
if __name__ == '__main__':
    testbench()