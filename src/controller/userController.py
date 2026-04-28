# Import
import json
from src.models.user import User, SuperUser

# Class
class UserManager:
    def __init__(self):
        self.__all_users = {'user_accounts' : [], 'superuser_accounts' : []}
        self.__autenticated_users = {}

        self.read('user_accounts')
        self.read('superuser_accounts')

    def read(self,database):
        account_class = SuperUser if (database == 'superuser_accounts') else User
        try:
            with open(f"src/controller/data/{database}.json", "r") as FILE:
                usr_data = json.load(FILE)
                self.__all_users[database] = [account_class(**data) for data in usr_data]
        except FileNotFoundError:
            self.__all_users[database].append(account_class('guest', "000", "", "", ""))

    def __write(self, database):
        try:
            with open(f"src/controller/data/{database}.json", "w") as FILE:
                usr_data = [vars(usr_account) for usr_account in self.__all_users[database]]
                json.dump(usr_data,FILE)
                print(f"Aquivo '{database}.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError(f"O sistema não conseguiu gerar o arquivo '{database}.json'.")

    def createUser(self,username,psswrd,cpf,email,contact,perms):
        usr_type = 'superuser_accounts' if perms else 'user_accounts'
        usr_class = SuperUser if perms else User

        new_usr = usr_class(username,psswrd,cpf,email,contact,perms) if perms else usr_class(username,psswrd,cpf,email,contact)
        self.__all_users[usr_type].append(new_usr)
        self.__write(usr_type)

        return new_usr.username

    def removeUser(self,user):
        for usr_type in ['user_accounts','superuser_accounts']:
            if user in self.__all_users:
                isSuper = ('(super)' if usr_type == 'superuser_accounts' else '')
                print(f"O usuário {isSuper}{user.username} foi encontrado no sistema.")

                self.__all_users[usr_type].remove(user)
                print(f"O usuário {isSuper}{user.username} foi removido do sistema.")

                self.__write(usr_type)
                return user.username
        print(f"O usuário {user.username} não foi encontrado no sistema.")
        return None

    def getUserAccounts(self):
        return self.__all_users['user_accounts']

    def getCurrentUser(self,session_id):
        if session_id in self.__autenticated_users:
            return self.__autenticated_users[session_id]
        else:
            return None

    def autenticateUser(self,cpf,psswrd):
        for usr_type in ['user_accounts','superuser_accounts']:
            for user in self.__all_users[usr_type]:
                if user.cpf == cpf and user.password == psswrd:
                    session_id = '123456' # coloca um sistema de gerar id, o HG usou uuid.uuid4()
                    self.__autenticated_users[session_id] = user
                    return session_id # retorna o ID para o user
        return None

    def logout(self, session_id):
        if session_id in self.__autenticated_users:
            del self.__autenticated_users[session_id] # remove o user logado

# Test bench
def testbench():
    print('Rodando Modo Teste')

if __name__ == '__main__':
    testbench()
