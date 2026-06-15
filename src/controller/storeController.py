class StoreManager:
    def __init__(self,productsmanager_instance,cartsmanager_instance):
        self._product_manager = productsmanager_instance
        self._cart_manager = cartsmanager_instance

    def create_product(self,data:list):
        if data:
            instance = self._product_manager.add_to_stock(data[0],data[1],data[2],data[3])
            return instance
        return None

    def edit_product_data(self,product_id:str,data:list):
        if product_id and data:
            self._product_manager.edit_on_stock(product_id, data[0], data[1], data[2], data[3])

    def delete_product(self,product_id:str):
        if product_id:
            event1 = self._product_manager.remove_from_stock(product_id)
            if event1:
                return True
        return False

    def get_product(self,product_id:str):
        if product_id:
            return self._product_manager.get_product_by_id(product_id)
        else:
            return None

    def get_all_products(self):
        return self._product_manager.get_products()

    def get_user_cart_products(self,owner_id:str):
        if owner_id:
            products = self._cart_manager.get_user_cart_products(owner_id)
            cart_data = []
            for key,value in list(products.items()):
                product = self.get_product(key)
                if product:
                    cart_data.append({
                        "name": product.name,
                        "product_id": product.product_id,
                        "quantity": value,
                        "unity_price": product.price,
                        "total_price": float(product.price * value)
                    })
                else:
                    self._cart_manager.remove_from_cart(owner_id,key)
            return cart_data
        return None

    def add_to_user_cart(self,data:list):
        if data:
            return self._cart_manager.add_to_user_cart(data[0],data[1],data[2])
        return False

    def remove_from_user_cart(self,owner_id:str,product_id:str):
        if owner_id and product_id:
            return self._cart_manager.remove_from_cart(owner_id,product_id)
        return False

    def get_product_quantity(self,owner_id:str,product_id:str):
        if not owner_id or not product_id:
            return None
        products = self._cart_manager.get_user_cart_products(owner_id)
        quantity = products.get(product_id, 0)
        return quantity