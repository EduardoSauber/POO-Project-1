# Import
import json
import uuid

from src.models.user import User, SuperUser

# Class
class UserManager:
    def __init__(self,data_path):
        self.__all_users = {'user_accounts' : [], 'superuser_accounts' : []}
        self.__authenticated_users = {}
        self.__DATA_PATH = data_path

        self.read('user_accounts')
        self.read('superuser_accounts')

    # -- Leitura e Escrita Banco de Dados -- #
    def read(self,database):
        account_class = SuperUser if (database == 'superuser_accounts') else User
        try:
            with open(f"{self.__DATA_PATH}/{database}.json", "r") as FILE:
                usr_data = json.load(FILE)
                self.__all_users[database] = [account_class(**data) for data in usr_data]
        except FileNotFoundError:
            print("userController: Não foi encontrado um banco de dados de clientes.")
            #self.__all_users[database].append(account_class('guest', "000", "00", "", ""))

    def __write(self, database):
        try:
            with open(f"{self.__DATA_PATH}/{database}.json", "w") as FILE:
                usr_data = [usr_account.to_dict() for usr_account in self.__all_users[database]]
                json.dump(usr_data,FILE)
                print(f"userController: Aquivo '{database}.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError(f"userController: O sistema não conseguiu gerar o arquivo '{database}.json'.")

    # -- Manuseamento de usuários -- #
    def create_user(self,username,psswrd,cpf,email,contact,perms):
        user_type = None

        if cpf is None:
            print("Valor 'cpf' não pode ser nulo.")
            return None
        if self.get_user_account(cpf) is not None:
            print(f"userController: Já existe um usuário com ID '{cpf}'.")
            return None

        if perms:
            user_type = 'superuser_accounts'
            new_user = SuperUser(username,psswrd,cpf,email,contact,perms)
        else:
            user_type = 'user_accounts'
            new_user = User(username,psswrd,cpf,email,contact)

        self.__all_users[user_type].append(new_user)

        self.__write(user_type)

        print("userController: Usuário cadastrado no sistema com exito.")
        return new_user

    def modify_user(self,user_id:str,n_username=None,n_pswrd=None,n_cpf=None,n_mail=None,n_contact=None):
        user = self.get_user_account(user_id)
        user_type = ('superuser_accounts' if user.is_admin() else 'user_accounts')

        if user is not None:
            if n_username:
                user.username = n_username
            if n_pswrd:
                user.password = n_pswrd
            if n_cpf:
                user.cpf = n_cpf
            if n_mail:
                user.email = n_mail
            if n_contact:
                user.contact = n_contact
            self.__write(user_type)
        else:
            print(f"userController: Nenhum usuário com ID '{user_id}' encontrado no sistema")

    def remove_user(self,user_id:str): # dá pra utilizar o get_user_account
        for user_type in ['user_accounts','superuser_accounts']:
            for index, user in enumerate(self.__all_users[user_type]):
                if user.cpf == user_id:
                    is_super = '(Super)' if user_type == 'superuser_accounts' else ''
                    print(f"userController: O usuário '{is_super}'{user.username} foi removido do sistema.")
                    del self.__all_users[user_type][index]
                    self.__write(user_type)
                    return
        print(f"userController: Usuário {user_id} não foi encontrado no sistema.")


    def get_user_accounts(self):
        return self.__all_users.get("user_accounts")

    def get_superuser_accounts(self):
        return self.__all_users.get("superuser_accounts")

    def get_user_account(self,user_id:str):
        for user_type in ['user_accounts','superuser_accounts']:
            for user in self.__all_users[user_type]:
                if user.cpf == user_id:
                    return user
        return None

    def get_session_id_user(self,session_id):
        return self.__authenticated_users.get(session_id)

    def get_username(self,session_id:str): # !!! possivelmente uma função inutil !!!
        user = self.get_session_id_user(session_id)
        return user.username if user else None

    def get_user_session_id(self,user_id:str):
        for session_id in self.__authenticated_users:
            if user_id == self.__authenticated_users[session_id].cpf:
                return session_id
        return None

    def get_session_permissions(self, session_id):
        if session_id:
            user = self.__authenticated_users.get(session_id)

            if user and hasattr(user,'permissions'):
                return user.permissions
        return []

    def authenticate_user(self, cpf:str, psswrd:str):
        user = self.get_user_account(cpf)

        if user is not None and user.check_password(psswrd):
            session_id = uuid.uuid4().hex
            self.__authenticated_users[session_id] = user
            return session_id

        return None

    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id] # remove o user logado

# Test bench
def testbench():
    print('Rodando Modo Teste\n\n')

    testeManager = UserManager("./data")

    print(testeManager.create_user("dinossarro","123","1234","teste@mail","333",False))
    print(testeManager.create_user("user123", "123", "7785", "teste@mail", "333", False))
    testeManager.modify_user("7785","SAUBIO")

    print(testeManager.create_user("adminossarro","123","6789","teste@mail","333", ['admin']))

    for testeuser in testeManager.get_user_accounts():
        print(testeuser)


if __name__ == '__main__':
    testbench()
