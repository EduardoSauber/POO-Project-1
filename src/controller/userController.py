# Import
import json
from src.models.user import User, SuperUser

# Class
class userManager:
    def __init__(self):
        self.__allusers = {'user_accounts' : [], 'superuser_accounts' : []}
        self.__autenticated_users = {}

        #carregar as contas normais e super

    def read(self,database):
        account_class = SuperUser if (database == 'superuser_accounts') else User
        try:
            with open(f"src/controller/data/{database}.json", "r") as file:
                usr_data = json.load(file)
                self.__allusers[database] = [account_class(**data) for data in usr_data]
        except FileNotFoundError:
            self.__allusers[database].append(account_class('guest',"000","","",""))

    def write(self,database):
        try:
            with open(f"src/controller/data/{database}.json", "w") as file:
                usr_data = [vars(UserAccount)]
        except FileNotFoundError:
            raise TypeError(f"O sistema não conseguiu gerar o arquivo {database}.")

    def createUser(self,username,psswrd,email,contact,perms):
        usr_type = 'superuser_accounts' if perms else 'user_accounts'
        usr_class = SuperUser if perms else User

        new_usr = usr_class(username,psswrd,email,contact,perms) if perms else usr_class(username,psswrd,email,contact)
        self.__allusers[usr_type].append(new_usr)
        self.write(usr_type)

        return new_usr.username

    def removeUser(self,user):
        for usr_type in ['user_accounts','superuser_accounts']:
            if user in self.__allusers:
                isSuper = ('(super)' if usr_type == 'superuser_accounts' else '')
                print(f"O usuário {isSuper}{user.username} foi encontrado no sistema.")

                self.__allusers[usr_type].remove(user)
                print(f"O usuário {isSuper}{user.username} foi removido do sistema.")

                self.write(usr_type)
                return user.username
        print(f"O usuário {user.username} não foi encontrado no sistema.")
        return None

    def getUserAccounts(self):
        pass

    def getCurrentUser(self):
        pass

    def autenticateUser(self,username,psswrd):
        for usr_type in ['user_accounts','superuser_accounts']:
            for user in self.__allusers[usr_type]:
                if user.username == username and user.password == psswrd:
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
