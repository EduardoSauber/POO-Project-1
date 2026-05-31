import getpass
from os import name


class AuthView:
    def __init__(self,app):
        self._app = app

    def main_menu(self):
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
                return "STOP"
            case _:
                print("Opção inválida!")

    def login_page(self):
        while self._app.personal_session_id is None:
            print("--- LOGAR ---")
            try:
                user_id = input("Digite seu CPF: ")
                user_password = getpass.getpass("Digite sua senha: ")
                self._app.login(user_id, user_password)
                if self._app.personal_session_id is not None:
                    return
            except ValueError as error:
                print(f"Erro: {error}. Tente novamente.")

    def signin_page(self):
        finalized = False
        while finalized == False:
            print("--- CADASTRAR-SE ---")

            name = None
            while True:
                print("Digite o nome de usuário (não pode conter números ou simbolos):")
                inpt = input().strip()
                if inpt and inpt.replace(" ","").isalpha():
                    name = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            cpf = None
            while True:
                print("Digite seu CPF (sem pontuação):")
                inpt = input().strip().replace("-","").replace(".","")
                if inpt and inpt.replace(" ","").isnumeric() and len(inpt) == 11:
                    cpf = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            email = None
            while True:
                print("Digite seu e-mail:")
                inpt = input().strip()
                if inpt and "@" in inpt and "." in inpt:
                    email = inpt
                    break
                else:
                    print("Entrada inválida! Tente novamente.")

            contact = None
            while True:
                print("Digite seu número de contato (Com DDD e 9, sem pontuações):")
                inpt = input().strip().replace("-", "").replace(" ","")
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

            user = self._app.signin([name,password,cpf,email,contact])
            if user:
                finalized = True