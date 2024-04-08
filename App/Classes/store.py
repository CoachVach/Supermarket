class Store:

    def __init__(self, products=[]):
        self.products = products

    def products_data(self):
        products = []
        for product in self.products:
            products.append((product.name, product.price, product.sell_price, product.market_price, product.stock, product.in_box, product.image))

        return products
    
    def get_product(self, name):
        for p in self.products:
            if p.name == name:
                return p
        return None