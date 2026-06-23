########################################################################################################################
# Import
import json
from src.models.product import Product

########################################################################################################################
# Class
class ProductManager:
    def __init__(self,data_path):
        self.__all_products= []
        self.__DATA_PATH = data_path

        self.__read()

    def __read(self):
        try:
            with open(f"{self.__DATA_PATH}/products.json", "r") as FILE:
                prdct_data = json.load(FILE)
                self.__all_products = [Product(**data) for data in prdct_data]
        except FileNotFoundError:
            pass
            print("productController: Não foi encontrado um banco de dados de produtos.")

    def __write(self):
        try:
            with open(f"{self.__DATA_PATH}/products.json", "w") as FILE:
                prdct_data = [product.to_dict() for product in self.__all_products]
                json.dump(prdct_data, FILE)
                print(f"productController: Aquivo 'products.json' gravado com exito.")
        except FileNotFoundError:
            raise TypeError(f"productController: O sistema não conseguiu gerar o arquivo 'products.json'.")

    def add_to_stock(self,product_name:str,product_id:str,price:float,quantity_to_stock:int):
        if product_id is not None:
            for items in self.__all_products:
                if items.product_id == product_id:
                    print("Produto já existe no estoque.")
                    break
            else:
                novo_produto = Product(product_name,product_id,price,quantity_to_stock)
                self.__all_products.append(novo_produto)
                self.__write()
                return novo_produto

    def edit_on_stock(self,product_id=None,new_product_id=None,new_product_name=None,new_price=None,new_quantity=None):
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
        if product_id is None:
            return False

        for index,items in enumerate(self.__all_products):
            if items.product_id == product_id:
                del self.__all_products[index]
                self.__write()
                return True

        return False

    def get_product_by_id(self,product_id):
        if not product_id:
            return None

        for product in self.__all_products:
            if product.product_id == product_id:
                return product
        return None

    def get_products(self):
        return self.__all_products

########################################################################################################################
# Testbench

def testbench():
    Controller = ProductManager("./data")

    Controller.add_to_stock("Teste","codigoteste123",12.95,50)
    for item in Controller.get_products():
        print(item)
    Controller.edit_on_stock("codigoteste123",new_product_name="ProdutoTeste")
    for item in Controller.get_products():
        print(item)
    Controller.remove_from_stock("codigoteste123")
    for item in Controller.get_products():
        print(item)

if __name__ == "__main__":
    testbench()