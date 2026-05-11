########################################################################################################################
# import
from src.controller.userController import UserManager
from src.controller.productController import ProductManager
from src.controller.cartController import CartManager

########################################################################################################################
# class
class AppManager:
    def __init__(self):
        self.user_manager = UserManager()
        self.product_manager = ProductManager()
        self.cart_manager = CartManager()

        self.user_manager.create_user("ADMIN","admin123","0","admin@mail","0",['Admin'])

    # login/cadastro de usuário
    def login(self):
        pass

    def iniciar(self):

        self.login()

        while True:
            print("[ 1 ] - Gerenciamento de Clientes")
            print("[ 2 ] - Gerenciamento de Produtos")
            print("[ 3 ] - Modo Compra")
            print("[ 4 ] - Sair")
            opcao = input("Digite  a opção desejada: ")

            match opcao:
                case 1:
                    self.gerenciamento_clientes()
                case 2:
                    self.gerenciamento_produtos()
                case 3:
                    pass
                case 4:
                    break

    def gerenciamento_clientes(self):
        pass

    def gerenciamento_produtos(self):
        pass

