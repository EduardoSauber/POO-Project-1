########################################################################################################################
# import
from src.controller.userController import UserManager
from src.controller.productController import ProductManager
from src.controller.cartController import CartManager
from src.controller.storeController import StoreManager
from src.view.ViewRouter import ViewRouter

########################################################################################################################
# class
class AppManager:
    def __init__(self,file_path):
        self._user_manager = UserManager(file_path)
        self._product_manager = ProductManager(file_path)
        self._cart_manager = CartManager(file_path)
        self._store_manager = StoreManager(self._product_manager,self._cart_manager,file_path)

        self._view_router = ViewRouter(self)

        self._personal_session_id = None # mudar de lugar (provavelmente para a main)

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

    def start(self):
        self._view_router.start()

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

    def edit_user_data(self,user_id,data:list):
        if data:
            self._user_manager.modify_user(user_id,data[0],data[1],data[2],data[3],data[4])

    def delete_user(self,user_id):
        if not user_id:
            return False

        event = self._user_manager.remove_user(user_id)
        return event

    def get_user_by_sessionid(self,session_id):
        if session_id:
            return self._user_manager.get_session_id_user(session_id)
        return None

    def get_user_by_cpf(self,user_id:str):
        if user_id:
            return self._user_manager.get_user_account(user_id=user_id)
        return None

    def get_user_username(self,session_id):
        if session_id:
            return self._user_manager.get_username(session_id)
        return None

    def get_user_list(self):
        return self._user_manager.get_user_accounts()

    def get_superuser_list(self):
        return self._user_manager.get_superuser_accounts()

    # --- LOJA, PRODUTOS E CARRINHOS ---
    def finish_user_purchase(self,user_id:str):
        if not user_id:
            return None

        event = self._store_manager.make_purchase(user_id=user_id)
        return event

    def get_purchases(self):
        return self._store_manager.get_purchases()

    def create_product(self,data:list):
        if data:
            product = self._store_manager.create_product(data)
            return True if product else False
        return False

    def edit_product_data(self,product_id:str,data:list):
        if data and product_id:
            self._store_manager.edit_product_data(product_id, data)

    def delete_product(self,product_id:str):
        if product_id:
            event = self._store_manager.delete_product(product_id)
            return event
        return False

    def get_product(self,product_id:str):
        if product_id:
            return self._store_manager.get_product(product_id)
        return None

    def get_all_products(self):
        return self._store_manager.get_all_products()

    def get_cart_products(self,owner_id:str):
        if owner_id:
            return self._store_manager.get_user_cart_products(owner_id)
        return None

    def get_cart_product_quantity(self,owner_id:str,product_id:str):
        if owner_id and product_id:
            return self._store_manager.get_product_quantity(owner_id,product_id)
        return None

    def add_to_user_cart(self,data:list):
        if data:
            return self._store_manager.add_to_user_cart(data)
        return False

    def remove_from_user_cart(self,data:list):
        if data:
            return self._store_manager.remove_from_user_cart(data[0],data[1])
        return False

    def remove_qtd_from_user_cart(self,data:list):
        if data:
            return self._store_manager.remove_from_user_cart(data[0],data[1])
        return False