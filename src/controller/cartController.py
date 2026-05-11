########################################################################################################################
# Import
import json
from src.models.cart import UserCart

########################################################################################################################
# Class
class CartManager:
    def __init__(self):
        self.__all_carts = [] #verifica dps se realmente é '__'

    # Leitura e Escrita de Banco de Dados
    def read(self):
        try:
            with open('src/controller/data/user_cars.json','r') as FILE:
                user_cart = json.load(FILE)
                self.__all_carts = [UserCart(**cart) for cart in user_cart]
        except FileNotFoundError:
            print("Não foi possível encontrar um banco de dados para 'user_carts'.")

    def __write(self):
        try:
            with open('src/controllers/data/user_carts.json','w') as FILE:
                user_cart = [vars(user_cart) for user_cart in self.__all_carts]
                json.dump(user_cart,FILE)
                print("Exito ao gerar arquivo 'user_carts.json'.")
        except FileNotFoundError:
            raise TypeError("Erro ao gerar arquivo 'user_carts.json'.")

    # Manuseamento de carrinho
    def create_cart(self, user_id):
        new_cart = UserCart(user_id)
        self.__all_carts.append(new_cart)
        #self.__write()
        #return new_cart

    def remove_cart(self):
        pass

    def add_to_cart(self, owner_id:str, product_id:str, quantity:int):
        if owner_id is not None:
            for cart in self.__all_carts:
                if cart.owner == owner_id:
                    cart.add_product({'product_id':product_id,'quantity':quantity})
                    print(cart.products)
                    break
            else:
                # poderia criar um cartzinho nesse caso
                print("Não existe carrinho para o usuário especificado.")

    def remove_from_cart(self, owner_id, product_id):
        if owner_id is not None:
            for cart in self.__all_carts:
                if cart.owner == owner_id:
                    cart.remove_product(product_id)
                    print(cart.products)
                    break

    def get_user_cart(self, owner_id):
        return [item for item in self.__all_carts if item.owner == owner_id]

########################################################################################################################
# Testbench

def testbench():
    print("Rodando Modo Teste!\n\n")

    testeManager = CartManager()

    testeManager.create_cart("123")
    testeManager.add_to_cart("123", "produto123", 5000)
    testeManager.add_to_cart("123", "nugget-e-mimosa", 30)
    testeManager.add_to_cart("456", "produto123", 30)

    testeManager.add_to_cart("123", "produto123", 40)

    testeManager.remove_from_cart("123", "nugget-e-mimosa")


if __name__ == '__main__':
    testbench()