class AdminView:
    def __init__(self,app):
        self._app = app

    def main_menu(self):
        print("--- Painel de Administração ---")

        perms = self._app.personal_permissions

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
                return "LOGOUT"
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