class User:
    def __init__(self,username,psswrd,cpf,email,contact):
        self.username = username
        self.password = psswrd
        self.cpf = cpf
        self.email = email
        self.contact = contact

    def isAdmin(self):
        return False

class SuperUser(User):
    def __init__(self,username,psswrd,cpf,email,contact,permissions):
        super().__init__(username,psswrd,cpf,email,contact)
        self.permissions = permissions
        if not permissions:
            self.permissions = ['user']

        def isAdmin(self):
            return True

