import getpass

class AdminView:
    def __init__(self,app):
        self._app = app

    def main_menu(self):
        print("--- Painel de Administração ---")

        perms = self._app.personal_permissions

        print("[ 1 ] - Ver Catálogo de Produtos")
        print("[ 2 ] - Ver Relatório de Vendas")
        if 'cashier' in perms or 'admin' in perms:
            print("-- Operações de Caixa --")
            print("[ 3 ] - Processar Venda Física")
            print("[ x ] - [W.I.P]")
        if 'admin' in perms:
            print("-- Gerenciamento de Sistema --")
            print("[ 4 ] - Gerenciar Administradores")
            print("[ 5 ] - Gerenciar Clientes")
            print("[ 6 ] - Gerenciar Estoque")
        print("-- Sistema --")
        print("[ 0 ] - Sair")

        opcao = input("Opção: ")
        match opcao:
            case '1':
                self.products_catalog()
            case '2':
                self.sales_record()
            case '3':
                self.process_sale()
            case '4':
                if 'admin' in perms:
                    self.manage_admins()
                else:
                    print("Opção inválida!")
            case '5':
                if 'admin' in perms:
                    self.manage_users()
                else:
                    print("Opção inválida!")
            case '6':
                if 'admin' in perms:
                    self.manage_products()
                else:
                    print("Opção inválida!")
            case '0':
                return "LOGOUT"
            case _:
                print("Opção inválida!")

    def products_catalog(self):
        # storeView cuida dessa parte
        pass

    def sales_record(self):
        # talvez storeView
        pass

    def process_sale(self):
        # storeView
        pass

    def manage_admins(self):
        aberto = True
        while aberto == True:
            print("[ 1 ] - Listar Administradores")
            print("[ 2 ] - Adicionar Administrador")
            print("[ 3 ] - Editar Administrador")
            print("[ 4 ] - Remover Administrador")
            print("[ 0 ] - Sair")
            opcao = input("Opção: ")
            match opcao:
                case '1':
                    pass
                case '2':
                    self.add_admin()
                case '3':
                    pass
                case '4':
                    pass
                case '0':
                    aberto = False
                case _:
                    print("Opção inválida!")

    def list_admins(self):
        pass

    def add_admin(self):
        finalized = False
        while finalized == False:
            print("--- CADASTRAR-SE ---")
            print("Digite 'sair' para cancelar o cadastro.\nNão é possível cancelar durante a senha.\n")

            name = None
            while True:
                print("Digite o nome de usuário (não pode conter números ou simbolos):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt and inpt.replace(" ", "").isalpha():
                    name = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            cpf = None
            while True:
                print("Digite seu CPF (sem pontuação):")
                inpt = input().strip().replace("-", "").replace(".", "")
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt and inpt.replace(" ", "").isnumeric() and len(inpt) == 11:
                    cpf = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            email = None
            while True:
                print("Digite seu e-mail:")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt and "@" in inpt and "." in inpt:
                    email = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            contact = None
            while True:
                print("Digite seu número de contato (Com DDD e 9, sem pontuações):")
                inpt = input().strip().replace("-", "").replace(" ", "")
                if inpt.lower() == "sair":
                    print("Cadastro Cancelado.")
                    finalized = True
                    return
                if inpt.isnumeric() and len(inpt) == 11:
                    contact = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            password = None
            while True:
                print("Digite sua senha (Pelo menos 5 caracteres, sem espaços):")
                inpt = getpass.getpass("")
                if inpt and len(inpt) > 4:
                    password = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            password_chk = None
            while True:
                print("Confirme sua senha:")
                inpt = getpass.getpass("")
                if inpt == password:
                    password_chk = inpt
                    break
                else:
                    print("Senhas não coincidem! Tente novamente.")

            permissions = None
            while permissions is None:
                print("Qual a função do Admin?")
                print("[ 1 ] - Caixa")
                print("[ 2 ] - Administrador")
                inpt = input()
                if inpt and inpt.isdigit():
                    match inpt:
                        case "1":
                            permissions = ["cashier"]
                        case "2":
                            permissions = ["admin"]
                        case _:
                            print("Entrada inválida! Tente novamente.")
                else:
                    print("Entrada inválida! Tente novamente.")


            user = self._app.signin([name, password, cpf, email, contact, permissions])
            if user:
                finalized = True

    def manage_users(self):
        pass

    def manage_products(self):
        # storeView cuida dessa parte
        pass