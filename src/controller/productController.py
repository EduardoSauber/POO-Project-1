# Import
import json
from src.models.product import Product
from src.models.cart import UserCart

# Class
class ProductManager:
    pass

class CartManager:
    def __init__(self):
        self.__all_carts = []

    def read(self):
        try:
            with open(f"src/controller/data/user_carts.json", 'r') as FILE:
                usr_cart = json.load(FILE)
                self.__all_carts = [UserCart(**cart) for cart in usr_cart]
        except FileNotFoundError:
            print("Não existem carrinhos registrados.")

    def __write(self):
        try:
            with open('src/controllers/data/user_carts.json', 'w') as FILE:
                usr_cart = [vars(usr_cart) for usr_cart in self.__all_carts]
                json.dump(usr_cart,FILE)
                print("Arquivo 'user_carts.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError("O sistema não conseguiu gerar o arquivo 'user_carts.json'.")

    def addToCart(self,cpf,product,quantity=1):
        new_cart_item = UserCart(cpf,product,quantity)
        self.__all_carts.append(new_cart_item)
        self.__write()
        return new_cart_item

    def getUserCart(self,cpf):
        return [item for item in self.__all_carts if item.cpf == cpf]

