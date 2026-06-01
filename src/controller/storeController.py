# controle de vendas
class StoreManager:
    def __init__(self,productsmanager_instance,cartsmanager_instance):
        self._product_manager = productsmanager_instance
        self._cart_manager = cartsmanager_instance

    def create_product(self,data:list):
        if data:
            instance = self._product_manager.add_to_stock(data[0],data[1],data[2],data[3])
            return instance

    def get_product(self,product_id):
        if product_id:
            pass

    def get_all_products(self):
        return self._product_manager.get_products()