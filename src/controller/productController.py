########################################################################################################################
# Import
import json
from src.models import cart
from src.models.product import Product
from src.models.cart import UserCart

########################################################################################################################
# Class
class ProductManager:
    def __init__(self,data_path):
        self.__all_products= []
        self.__DATA_PATH = data_path

        self.read()

    def read(self):
        try:
            with open(f"{self.__DATA_PATH}/products.json", "r") as FILE:
                prdct_data = json.load(FILE)
                self.__all_products = [Product(**data) for data in prdct_data]
        except FileNotFoundError:
            print("productController: Não foi encontrado um banco de dados de produtos.")

    def __write(self):
        try:
            with open(f"{self.__DATA_PATH}/products.json", "w") as FILE:
                prdct_data = [product.to_dict() for product in self.__all_products]
                json.dump(prdct_data, FILE)
                print(f"productController: Aquivo 'products.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError(f"productController: O sistema não conseguiu gerar o arquivo 'products.json'.")

    def add_to_stock(self,product_id:str,product_name:str,price:float,quantity_to_stock:int):
        if product_id is not None:
            for items in self.__all_products:
                if items.product_id == product_id:
                    print("Produto já existe no estoque.")
                    break
            else:
                novo_produto = Product(product_name,product_id,price,quantity_to_stock)
                self.__all_products.append(novo_produto)
                self.__write()

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
                    self.__write()
                    break
            else:
                print("Produto especificado não existe no banco de dados.")

    def remove_from_stock(self,product_id):
        if product_id is not None:
            for index,items in enumerate(self.__all_products):
                if items.product_id == product_id:
                    del self.__all_products[index]
                    self.__write()
                    break

    def get_product(self,product_id):
        pass

    def get_products(self):
        return self.__all_products

########################################################################################################################
# Testbench

def testbench():
    print("Rodando Modo Teste!")

    teste_products = ProductManager("./data")
    teste_products.add_to_stock("123","teste",50,50)

    for testeproduct in teste_products.get_products():
        print(testeproduct)

if __name__ == "__main__":
    testbench()