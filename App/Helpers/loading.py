from ..Classes.supermarket import Supermarket
from ..Classes.product import Product
from ..Classes.store import Store
from ..Classes.shelf import Shelf
from ..Classes.stock import Stock
from ..Interfaces.Tablet.store import StoreInterface

def load_market(interface_objects):
    money = 1000
    customers = []
    stock = Stock(interface_objects=interface_objects)
    
    market = Supermarket(stock=stock, money=money, customers=customers)

    return market

def load_products():
    apple = Product("Apple",5)
    wine = Product("Wine",16)
    pasta = Product("Pasta",10)
    chocolate = Product("Chocolate",8)
    water = Product("Water",10)

    return [apple, wine, pasta, chocolate, water]

def load_store():
    products = load_products()

    store = Store(products)

    return store

def load_store_interface(interface_objects):
    store = load_store()
    market = load_market(interface_objects)

    return StoreInterface(store,market)

def load_shelves():
    s1, s2, s3 = Shelf(), Shelf(), Shelf()

    s1.update_position(50, 100)
    s2.update_position(55, 300)
    s3.update_position(400, 350)

    return [s1,s2,s3]

def load_interface_objects(interface_objects):
    shelves = load_shelves()

    interface_objects.shelves = shelves

    return interface_objects