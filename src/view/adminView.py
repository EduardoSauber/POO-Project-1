import getpass
from subprocess import call
import os
from time import sleep

class AdminView:
    def __init__(self,app,storeview_instance):
        self._app = app
        self._store_view = storeview_instance

    def hold_menu(self, duration: int = 5):
        print(f"O menu fechará em {duration} segundo(s)...")
        sleep(duration)
        call('clear' if os.name == 'posix' else 'cls')

    def main_menu(self):
        print("--- Painel de Administração ---")

        perms = self._app.personal_permissions

        if 'admin' in perms:
            print("-- Gerenciamento de Sistema --")
            print("[ 1 ] - Gerenciar Administradores")
            print("[ 2 ] - Gerenciar Clientes")
            print("[ 3 ] - Gerenciar Estoque")
        print("-- Sistema --")
        print("[ 0 ] - Sair")

        opcao = input("Opção: ")
        match opcao:
            case '1':
                if 'admin' in perms:
                    self.manage_admins()
                else:
                    print("Opção inválida!")
            case '2':
                if 'admin' in perms:
                    self.manage_users()
                else:
                    print("Opção inválida!")
            case '3':
                if 'admin' in perms:
                    self.manage_products()
                else:
                    print("Opção inválida!")
            case '0':
                return "LOGOUT"
            case _:
                print("Opção inválida!")

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
                    self.list_admins()
                case '2':
                    self.add_user()
                case '3':
                    self.edit_user()
                case '4':
                    self.remove_user()
                case '0':
                    aberto = False
                case _:
                    print("Opção inválida!")

    def list_admins(self):
        superusers = self._app.get_superuser_list()
        for user in superusers:
            print(user)
        self.hold_menu()

    def manage_users(self):
        aberto = True
        while aberto == True:
            print("[ 1 ] - Listar Clientes")
            print("[ 2 ] - Adicionar Cliente")
            print("[ 3 ] - Editar Cliente")
            print("[ 4 ] - Remover Cliente")
            print("[ 0 ] - Sair")
            opcao = input("Opção: ")
            match opcao:
                case '1':
                    self.list_users()
                case '2':
                    self.add_user()
                case '3':
                    self.edit_user()
                case '4':
                    self.remove_user()
                case '0':
                    aberto = False
                case _:
                    print("Opção inválida!")

    def list_users(self):
        users = self._app.get_user_list()
        for user in users:
            print(user)

    def add_user(self):
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
                print("O usuário será Administrador?")
                print("[ 1 ] - Não")
                print("[ 2 ] - Sim")
                inpt = input()
                if inpt and inpt.isdigit():
                    match inpt:
                        case"1":
                            permissions = False
                        case "2":
                            permissions = ["admin"]
                        case _:
                            print("Entrada inválida! Tente novamente.")
                else:
                    print("Entrada inválida! Tente novamente.")


            user = self._app.signin([name, password, cpf, email, contact, permissions])
            if user:
                finalized = True

    def edit_user(self):
        finalized = False

        while finalized == False:
            print("--- Editar Dados do Usuário ---")

            user_id = None
            while True:
                print("Digite o CPF do Usuário (sem pontuação):")
                inpt = input().strip().replace("-", "").replace(".", "")
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt and inpt.replace(" ", "").isnumeric() and len(inpt) == 11:
                    user_id = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            user = self._app.get_user_by_cpf(user_id)
            if not user:
                print("Usuário não encontrado no sistema!")
                finalized = True
                return

            print("[ 1 ] - Editar Nome")
            print("[ 2 ] - Editar CPF")
            print("[ 3 ] - Editar E-mail")
            print("[ 4 ] - Editar Contato")
            print("[ 5 ] - Editar Senha")
            print("[ 0 ] - Sair")
            opcao = input("Opção: ")
            match opcao:
                case '1':
                    n_name = self.edit_user_name()
                    if n_name:
                        self._app.edit_user_data(user_id, [n_name, None, None, None, None])
                    finalized = True
                case '2':
                    n_cpf = self.edit_user_cpf()
                    if n_cpf:
                        self._app.edit_user_data(user_id, [None, None, n_cpf, None, None])
                    finalized = True
                case '3':
                    n_email = self.edit_user_email()
                    if n_email:
                        self._app.edit_user_data(user_id, [None, None, None, n_email, None])
                    finalized = True
                case '4':
                    n_contact = self.edit_user_contact()
                    if n_contact:
                        self._app.edit_user_data(user_id,[None, None, None, None, n_contact])
                    finalized = True
                case '5':
                    n_password = self.edit_user_password()
                    if n_password:
                        self._app.edit_user_data(user_id, [None, n_password, None, None, None])
                    finalized = True
                case '0':
                    aberto = False
                case _:
                    print("Opção inválida!")

    def edit_user_name(self):
        finalized = False
        while finalized == False:
            print("-- Editar nome de Usuário --")
            name = None
            while True:
                print("Digite novo nome de usuário (não pode conter números ou simbolos):")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt and inpt.replace(" ", "").isalpha():
                    name = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")
            return name

    def edit_user_cpf(self):
        finalized = False
        while finalized == False:
            cpf = None
            while True:
                print("Digite seu novo CPF (sem pontuação):")
                inpt = input().strip().replace("-", "").replace(".", "")
                if inpt.lower() == "sair":
                    print("Operação Cancelada.")
                    finalized = True
                    return
                if inpt and inpt.replace(" ", "").isnumeric() and len(inpt) == 11:
                    cpf = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")
            return cpf

    def edit_user_email(self):
        finalized = False
        while finalized == False:
            email = None
            while True:
                print("Digite seu novo e-mail:")
                inpt = input().strip()
                if inpt.lower() == "sair":
                    print("Operação Cancelada.")
                    finalized = True
                    return
                if inpt and "@" in inpt and "." in inpt:
                    email = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")
            return email

    def edit_user_contact(self):
        finalized = False
        while finalized == False:
            contact = None
            while True:
                print("Digite seu novo número de contato (Com DDD e 9, sem pontuações):")
                inpt = input().strip().replace("-", "").replace(" ", "")
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt.isnumeric() and len(inpt) == 11:
                    contact = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")
            return contact

    def edit_user_password(self):
        finalized = False
        while finalized == False:
            password = None
            while True:
                print("Digite sua nova senha (Pelo menos 5 caracteres, sem espaços):")
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
            return password_chk


    def remove_user(self):
        finalized = False
        while finalized == False:
            print("--- Remover Usuário ---")
            cpf = None
            while True:
                print("Digite o CPF do Usuário (sem pontuação):")
                inpt = input().strip().replace("-", "").replace(".", "")
                if inpt.lower() == "sair":
                    print("Operação cancelada.")
                    finalized = True
                    return
                if inpt and inpt.replace(" ", "").isnumeric() and len(inpt) == 11:
                    cpf = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            event = self._app.delete_user(cpf)
            if event:
                finalized = True
            else:
                continue


    def manage_products(self):
        aberto = True
        while aberto == True:
            print("[ 1 ] - Listar Produtos")
            print("[ 2 ] - Adicionar Produto")
            print("[ 3 ] - Editar Produto")
            print("[ 4 ] - Remover Produto")
            print("[ 0 ] - Sair")
            opcao = input("Opção: ")
            match opcao:
                case '1':
                    self._store_view.list_products()
                case '2':
                    self._store_view.create_product()
                case '3':
                    self._store_view.edit_product()
                case '4':
                    self._store_view.delete_product()
                case '5':
                    self._store_view.delete_product()
                case '0':
                    aberto = False
                case _:
                    print("Opção inválida!")