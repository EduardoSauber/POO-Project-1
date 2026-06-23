########################################################################################################################
# Import
import json
from src.models.cart import UserCart

########################################################################################################################
# Class
class CartManager:
    def __init__(self,data_path):
        self.__all_carts = []
        self.__DATA_PATH = data_path

        self.__read()

    # Leitura e Escrita de Banco de Dados
    def __read(self):
        try:
            with open(f"{self.__DATA_PATH}/carts.json", "r") as FILE:
                cart_data = json.load(FILE)
                self.__all_carts = [UserCart(**data) for data in cart_data]
        except FileNotFoundError:
            print("cartController: Não foi encontrado um banco de dados de carrinhos.")

    def __write(self):
        try:
            with open(f"{self.__DATA_PATH}/carts.json", "w") as FILE:
                cart_data = [cart.to_dict() for cart in self.__all_carts]
                json.dump(cart_data, FILE)
                print(f"cartController: Aquivo 'carts.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError(f"cartController: O sistema não conseguiu gerar o arquivo 'carts.json'.")

    # Manuseamento de carrinho
    def get_cart(self, user_id):
        for cart in self.__all_carts:
            if cart.owner == user_id:
                return cart

        new_cart = UserCart(user_id)
        self.__all_carts.append(new_cart)
        self.__write()
        return new_cart

    def remove_cart(self,owner_id):
        for index, cart in enumerate(self.__all_carts):
            if cart.owner == owner_id:
                del self.__all_carts[index]
                self.__write()
                break

    def add_to_user_cart(self, owner_id:str, product_id:str, quantity:int):
        if owner_id:
            cart = self.get_cart(owner_id)
            cart.add_product(product_id,quantity)
            self.__write()
            return True
        return False

    def remove_from_cart(self, owner_id, product_id):
        if owner_id is not None:
            for cart in self.__all_carts:
                if cart.owner == owner_id:
                    event = cart.remove_product(product_id)
                    self.__write()
                    return event
        return False

    def get_user_cart_products(self, owner_id):
        for cart in self.__all_carts:
            if cart.owner == owner_id:
                return cart.products
        return {}

########################################################################################################################
# Testbench

def testbench():
    Controller = CartManager("./data")

    print(Controller.get_cart("12345678912"))
    Controller.add_to_user_cart("12345678912","codigoteste123", 25)
    print(Controller.get_user_cart_products("12345678912"))
    Controller.remove_from_cart("12345678912","codigoteste123")
    print(Controller.get_user_cart_products("12345678912"))

    Controller.remove_cart("12345678912")

if __name__ == '__main__':
    testbench()