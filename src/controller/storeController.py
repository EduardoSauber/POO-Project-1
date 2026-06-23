# import
import json

# class
class StoreManager:
    def __init__(self,productsmanager_instance,cartsmanager_instance,data_path):
        self._product_manager = productsmanager_instance
        self._cart_manager = cartsmanager_instance

        self.__purchases = []
        self.__DATA_PATH = data_path

        self.__read()

    def __read(self):
        try:
            with open(f"{self.__DATA_PATH}/purchases.json", "r") as FILE:
                pur_data = json.load(FILE)
                self.__purchases = [data for data in pur_data]
        except FileNotFoundError:
            print("storeController: Não foi encontrado um banco de dados de produtos.")

    def __write(self):
        try:
            with open(f"{self.__DATA_PATH}/purchases.json", "w") as FILE:
                pur_data = [purchase for purchase in self.__purchases]
                json.dump(pur_data, FILE)
                print(f"storeController: Aquivo 'purchases.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError(f"storeController: O sistema não conseguiu gerar o arquivo 'purchases.json'.")

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
                    if value > product.stock:
                        value = product.stock

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

    def make_purchase(self,user_id:str):
        if not user_id:
            return None

        user_cart = self.get_user_cart_products(user_id)

        if user_cart:
            total_value = 0
            for product in user_cart:
                stock_product = self.get_product(product['product_id'])
                self._product_manager.edit_on_stock(product_id=product['product_id'],
                                                    new_quantity=stock_product.stock-product['quantity'])
                total_value += product['total_price']
            purchase_receipt = {
                "buyer_id":user_id,
                "items":user_cart,
                "total":total_value
            }
            self._cart_manager.remove_cart(user_id)
            self.__purchases.append(purchase_receipt)
            self.__write()
            return purchase_receipt
        return False

    def get_purchases(self):
        return self.__purchases
