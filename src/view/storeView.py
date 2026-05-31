class StoreView:
    def __init__(self, app):
        self._app = app

    def list_products(self):
        products = self._app.get_all_products()
        for product in products:
            print(product)