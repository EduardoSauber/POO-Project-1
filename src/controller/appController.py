########################################################################################################################
# import
from src.controller.userController import UserManager
from src.controller.productController import ProductManager
from src.controller.cartController import CartManager
from src.controller.storeController import StoreManager

########################################################################################################################
# class
class AppManager:
    def __init__(self,file_path):
        self._user_manager = UserManager(file_path)
        self._product_manager = ProductManager(file_path)
        self._cart_manager = CartManager(file_path)
        self._store_manager = StoreManager(self._product_manager,self._cart_manager)

        # achar um jeito melhor de criar um admin inicial
        #self._user_manager.create_user("ADMIN", "admin123", "99", "admin@mail", "0", ['admin'])

        self._personal_session_id = None

    @property
    def personal_session_id(self):
        return self._personal_session_id
    @personal_session_id.setter
    def personal_session_id(self,value):
        self._personal_session_id = value

    @property
    def personal_permissions(self):
        return self._user_manager.get_session_permissions(self.personal_session_id)

    @property
    def is_user_admin(self):
        if self.personal_session_id:
            return self._user_manager.get_session_id_user(self.personal_session_id).is_admin()
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
        if data:
            user = self._user_manager.create_user(data[0],data[1],data[2],data[3],data[4],data[5])
            return True if user else False
        return False

    def logout(self):
        self._user_manager.logout(self.personal_session_id)
        self.personal_session_id = None

    # --- LOJA, PRODUTOS E CARRINHOS ---
    def create_product(self,data:list):
        if data:
            product = self._store_manager.create_product(data)
            return True if product else False
        return False

    def get_product(self,product_id:str):
        if product_id:
            return self._store_manager.get_product(product_id)

    def get_all_products(self):
        return self._store_manager.get_all_products()


# testbench
'''
testbench somente pelo viewRouter.py
'''
