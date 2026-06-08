# controle de vendas
class StoreManager:
    def __init__(self,productsmanager_instance,cartsmanager_instance):
        self._product_manager = productsmanager_instance
        self._cart_manager = cartsmanager_instance

    def create_product(self,data:list):
        if data:
            instance = self._product_manager.add_to_stock(data[0],data[1],data[2],data[3])
            return instance
        return None

    def delete_product(self,product_id:str):
        if product_id:
            event1 = self._product_manager.remove_from_stock(product_id)
            event2 = self._cart_manager.remove_from_all_carts(product_id)
            if event1:
                if not event2:
                    print("StoreManager: Erro ao remover produto deletado dos carrinhos!")
                return True
        return False

    def get_product(self,product_id:str):
        if product_id:
            return self._product_manager.get_product_by_id(product_id)
        else:
            return None

    def get_all_products(self):
        return self._product_manager.get_products()

    def add_to_user_cart(self,data:list):
        if data:
            return self._cart_manager.add_to_user_cart(data[0],data[1],data[2])
        return False