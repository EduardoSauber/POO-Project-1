########################################################################################################################
# import
from getpass import getpass

from src.controller.userController import UserManager
from src.controller.productController import ProductManager
from src.controller.cartController import CartManager

########################################################################################################################
# class
class AppManager:
    def __init__(self):
        self._user_manager = UserManager()
        self._product_manager = ProductManager()
        self._cart_manager = CartManager()

        # achar um jeito melhor de criar um admin inicial
        self._user_manager.create_user("ADMIN", "admin123", "99", "admin@mail", "0", ['admin'])

        self.personal_session_id = None
    @property
    def is_user_admin(self):
        if self.personal_session_id:
            return self._user_manager.get_session_id_user(self.personal_session_id).isAdmin()
        else:
            return False
    # --- LOGIN E CADASTRO DE USUARIO ---
    def login(self,user_id,password):
        check_session_id = self._user_manager.authenticate_user(user_id,password)
        if check_session_id:
            self.personal_session_id = check_session_id
            print("Usuário logado com exito.")
            return True
        else:
            print("Acesso negado. Tente novamente.")
            return False

    def signin(self,data:list):
        '''
        data = [nome,senha,cpf,email,contato]
        '''
        pass

# testbench
def testbench():
    print("Rodando modo teste:")
if __name__ == '__main__':
    testbench()
