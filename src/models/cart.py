########################################################################################################################
# Import


########################################################################################################################
# Class
class UserCart:
    def __init__(self,owner_id:str,products:dict = None):
        self._owner = owner_id

        #self._products = {} # {'product_id': quantity}
        if products is not None:
            self._products = products
        else:
            self._products = {}

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

    def add_product(self,product_id:str,quantity: int):
        if product_id:
            if product_id in self._products:
                self._products[product_id] += quantity
            else:
                self._products[product_id] = quantity

    def remove_product(self,product_id:str):
        if product_id:
            if product_id in self._products:
                del self._products[product_id]

    def to_dict(self):
        return {
            "owner_id": self._owner,
            "products": self._products
        }

########################################################################################################################
# Testbench
def testbench():
    pass

if __name__ == '__main__':
    testbench()