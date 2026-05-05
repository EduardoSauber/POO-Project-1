########################################################################################################################
# Import


########################################################################################################################
# Class
class UserCart:
    def __init__(self,owner_id:str):
        self._owner = None
        self._products = [] # {'product_id','quantity'}

        self.owner = owner_id
        # self.add_product(product) R.I.P

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value:str):
        if value is not None and value.isdigit():
            self._owner = value
        else:
            raise TypeError("")

    @property
    def products(self):
        return self._products

    def add_product(self,value:dict):
        if isinstance(value, dict):
            # verificar se o produto já existe
            self._products.append(value)
        else:
            raise TypeError("O valor inserido deve ser um dicionário.")

    def remove_product(self,product_id:str):
        if isinstance(product_id,str):
            for index, product in enumerate(self._products):
                if product.get('product_id') == product_id:
                    del self._products[index]
                    break
        else:
            raise TypeError("O ID de produto deve ser uma string de números!")

########################################################################################################################
# Testbench
def testbench():
    testeProduto = dict(product_id="12345",quantity=35)
    testeProduto2 = dict(product_id="67891",quantity=10000)

    testeCarrinho = UserCart("123")

    testeCarrinho.add_product(testeProduto)
    print(testeCarrinho.products)
    testeCarrinho.add_product(testeProduto2)
    print(testeCarrinho.products)

    testeCarrinho.remove_product("12345")
    print(testeCarrinho.products)

    testeVars = vars(testeCarrinho)
    print(testeVars)

if __name__ == '__main__':
    testbench()