########################################################################################################################
# Class
class User:
    def __init__(self,username:str,password:str,cpf:str,email:str,contact:str):
        self._username = username
        self.__password = password # criptografar a senha dps
        self._cpf = cpf
        self._email = email
        self._contact = contact
    def __str__(self):
        return f"Usuário: {self.username} | CPF: {self.cpf} | E-mail: {self.email} | Contato: {self.contact}"

    # Propriedades
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,value:str):
        if value is not None and isinstance(value,str):
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
            raise TypeError("O cpf deve ser um string de números!")

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
    def to_dict(self):
        return {
            "username": self._username,
            "password": self.__password,
            "cpf": self._cpf,
            "email": self._email,
            "contact": self._contact
        }
    def is_admin(self):
        return False

    def check_password(self,value:str):
        return self.__password == value

class SuperUser(User):
    def __init__(self,username,password,cpf,email,contact,permissions):
        super().__init__(username,password,cpf,email,contact)
        self._permissions = permissions
        if not permissions:
            self._permissions = ['user']
    def __str__(self):
        return f"Usuário: {self.username} | CPF: {self.cpf} | E-mail: {self.email} | Contato: {self.contact} | Perms: {self._permissions}"

    @property
    def permissions(self):
        return self._permissions

    def to_dict(self):
        data = super().to_dict()
        data["permissions"] = self._permissions

        return data

    def is_admin(self):
        return True
