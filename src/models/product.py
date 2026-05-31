class Product:
    def __init__(self,name,product_id,price,stock):
        self._name = name
        self._product_id = product_id
        self._price = price
        self._stock = stock

    # String de retorno
    def __str__(self):
        return f"Produto: {self.name} | ID: {self.product_id} | Preço: R${self.price:.2f} | Estoque: {self.stock}"

    # Propriedades
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value:str):
        if isinstance(value,str):
            self._name = value
        else:
            raise TypeError("O valor inserido deve ser uma string!")

    @property
    def product_id(self):
        return self._product_id
    @product_id.setter
    def product_id(self,value:str):
        if value.isdigit():
            self._product_id = value
        else:
            raise TypeError("O valor inserido deve ser uma string de números!")

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value:float):
        if  isinstance(value,float):
            self._price = value
        else:
            raise TypeError("O valor inserido deve ser um float!")

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,value:int):
        if isinstance(value,int):
            self._stock = value
        else:
            raise TypeError("O valor inserido deve ser um integer!")

    def to_dict(self):
        return {
            "name":self.name,
            "product_id":self.product_id,
            "price":self.price,
            "stock":self.stock
        }

########################################################################################################################
# Testbench
def testbench():
    testeProduto = Product("Fortnite","12345",15.90,50)
    print(testeProduto)
    testeProduto.price = 5.50
    testeProduto.stock = 4
    print(testeProduto)


if __name__ == '__main__':
    testbench()

