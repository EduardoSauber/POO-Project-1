class User:
    def __init__(self,username,psswrd,email,contact):
        self.username = username
        self.password = psswrd
        self.email = email
        self.contact = contact

        '''
        Adicionar o sistema de carrinho
        '''
        #self.cart = []

    def isAdmin(self):
        return False

class SuperUser(User):
    def __init__(self,username,psswrd,email,contact,permissions):
        super().__init__(username,psswrd,email,contact)
        self.permissions = permissions
        if not permissions:
            self.permissions = ['user']

        def isAdmin(self):
            return True

