from App.Classes.cash_register import CashRegister
from App.Classes.customer import Customer
from App.Classes.player import Player
from App.Helpers.matrix_creation_helper import create_matrix
from App.Interfaces.Tablet.stock import StockInterface
from App.Interfaces.interface_objects import InterfaceObjects
from ...Classes.supermarket import Supermarket
from ...Classes.product import Product
from ...Classes.store import Store
from ...Classes.shelf import Shelf
from ...Classes.stock import Stock
from ...Interfaces.Tablet.store import StoreInterface

def load_new_game(screen):
    interface_objects = InterfaceObjects(screen)
    store_interface = load_store_interface(interface_objects)
    interface_objects = load_interface_objects(interface_objects)
    matrix = create_matrix(interface_objects.shelves)
    player = Player(matrix)
    customers = load_customers(matrix, store_interface.supermarket)
    stock_interface = StockInterface(store_interface.supermarket.stock)
    
    return interface_objects, store_interface, matrix, player, customers, stock_interface

def load_market(interface_objects, money = 1000):
    stock = Stock(interface_objects=interface_objects)
    
    market = Supermarket(stock=stock, money=money)

    return market

def load_products():
    apple = Product("Apple", 5, image="apple.png")
    wine = Product("Wine", 16, image="wine.png")
    pasta = Product("Pasta", 10, image="pasta.png")
    chocolate = Product("Chocolate", 8, image="chocolate.png")
    water = Product("Water", 10, image="water.png")

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

def load_cash_register():
    return CashRegister()

def load_customers(matrix, supermarket):
    c1 = Customer("Erik", matrix, supermarket)
    c2 = Customer("Robert", matrix, supermarket)
    c3 = Customer("Maria", matrix, supermarket)
    customers = [c1, c2, c3]
    return customers

def load_interface_objects(interface_objects):
    cash_register = load_cash_register()

    shelves = load_shelves()

    interface_objects.shelves = shelves
    interface_objects.cash_register = cash_register

    return interface_objects