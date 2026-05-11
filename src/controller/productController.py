########################################################################################################################
# Import
import json
from src.models import cart
from src.models.product import Product
from src.models.cart import UserCart

########################################################################################################################
# Class
class ProductManager:
    def __init__(self):
        self.__all_products= [] # recebe class Product

    def read(self):
        pass

    def __write(self):
        pass

    def add_to_stock(self,product_id:str,product_name:str,price:float,quantity_to_stock:int):
        if product_id is not None:
            for items in self.__all_products:
                if items.product_id == product_id:
                    print("Produto já existe no estoque.")
                    break
            else:
                novo_produto = Product(product_name,product_id,price,quantity_to_stock)
                self.__all_products.append(novo_produto)
                #self.__write()

    def edit_on_stock(self,product_id,new_product_id,new_product_name,new_price,new_quantity):
        if product_id is not None:
            for items in self.__all_products:
                if items.product_id == product_id:
                    if new_product_id:
                        items.product_id = new_product_id
                    if new_product_name:
                        items.name = new_product_name
                    if new_price:
                        items.price = new_price
                    if new_quantity:
                        items.stock = new_quantity
                    #self.__write()
                    break
            else:
                print("Produto especificado não existe no banco de dados.")

    def remove_from_stock(self,product_id):
        if product_id is not None:
            for index,items in enumerate(self.__all_products):
                if items.product_id == product_id:
                    del self.__all_products[index]
                    #self.__write()
                    break

    def get_product(self,product_id):
        pass

    def get_products(self):
        return self.__all_products

########################################################################################################################
# Testbench

def testbench():
    print("Rodando Modo Teste!")

if __name__ == "__main__":
    testbench()