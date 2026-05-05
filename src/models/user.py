########################################################################################################################
# Class
class User:
    def __init__(self,username:str,psswrd:str,cpf:str,email:str,contact:str):
        self._username = None
        self.__password = None
        self._cpf = None
        self._email = None
        self._contact = None

        self.username = username
        self.password = psswrd
        self.cpf = cpf
        self.email = email
        self.contact = contact

    # string de retorno
    def __str__(self):
        return f"Usuário: {self.username} | CPF: {self.cpf} | E-mail: {self.email} | Contato: {self.contact}"

    # Propriedades
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,value:str):
        if value is not None and isinstance(value,str): # Talvez remover o caso None já que username não é tão importante
            self._username = value
        else:
            raise TypeError("O username deve ser um string!")

    @property
    def password(self):
        return None
    @password.setter
    def password(self,value:str):
        if value is not None and isinstance(value,str):
            self.__password = value
        else:
            raise TypeError("A password deve ser um string!")

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,value:str):
        if value is not None and value.isdigit():
            self._cpf = value
        else:
            raise TypeError("O user_id deve ser um string de números!")

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value:str):
        if isinstance(value,str):
            self._email = value
        else:
            raise TypeError("O email deve ser um string!")

    @property
    def contact(self):
        return self._contact
    @contact.setter
    def contact(self,value:str):
        if isinstance(value,str) and value.isdigit():
            self._contact = value
        else:
            raise TypeError("O contact deve ser um string de números!")

    # Métodos adicionais
    def isAdmin(self):
        return False

    def checkPassword(self,value:str):
        '''
        uma forma de verificar a senha de um usuário sem deixar a senha visível para o sistema inteiro
        '''
        return self.__password == value

class SuperUser(User):
    def __init__(self,username,psswrd,cpf,email,contact,permissions):
        super().__init__(username,psswrd,cpf,email,contact)
        self.permissions = permissions
        if not permissions:
            self.permissions = ['user']

    # string de retorno
    def __str__(self):
        return f"Usuário: {self.username} | CPF: {self.cpf} | E-mail: {self.email} | Contato: {self.contact} | Perms: {self.permissions}"

    def isAdmin(self):
        return True

########################################################################################################################
# Testbench

def testbench():
    userTeste = User("DinoSarro123","dinobambino","123456","dinossaro@email.ru","40028922")
    print(userTeste)
    print(userTeste.password)
    userTeste.password = "DinoBrewster"
    userTeste.username = "Dino Brewster"
    print(userTeste.password)
    print(userTeste)

    suserTeste = SuperUser("Tobey Marshall","pete4ever","2015","tobymrshall@nfs.mw","123456",['admin','DeLeon'])
    suserTeste2 = SuperUser("Finn","mr_robot","3778459","finn.nn","1234567",False)
    print(suserTeste)
    print(suserTeste2)

if __name__ == "__main__":
    testbench()
