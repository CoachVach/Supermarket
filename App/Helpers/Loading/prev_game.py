import sqlite3

from App.Classes.player import Player
from App.Classes.product import Product
from App.Classes.shelf import Shelf
from App.Classes.store import Store
from App.Helpers.Loading.new_game import load_cash_register, load_customers, load_market
from App.Helpers.matrix_creation_helper import create_matrix
from App.Interfaces.Tablet.stock import StockInterface
from App.Interfaces.Tablet.store import StoreInterface
from App.Interfaces.interface_objects import InterfaceObjects

def load_db(screen):
    conn = sqlite3.connect('game1.db')
    cursor = conn.cursor()

    interface_objects = InterfaceObjects(screen)
    store_interface = load_store_interface(interface_objects, cursor)
    interface_objects = load_interface_objects(interface_objects, cursor, store_interface)
    matrix = create_matrix(interface_objects.shelves)
    player = Player(matrix)
    customers = load_customers(matrix, store_interface.supermarket)
    stock_interface = StockInterface(store_interface.supermarket.stock)

    cursor.close()
    conn.close()

    return interface_objects, store_interface, matrix, player, customers, stock_interface

def load_interface_objects(interface_objects, cursor, store_interface):
    cash_register = load_cash_register()

    shelves = load_shelves(cursor, store_interface)

    interface_objects.shelves = shelves
    interface_objects.cash_register = cash_register

    return interface_objects

def load_shelves(cursor, store_interface):
    shelves_array = []

    cursor.execute('''SELECT * FROM shelves''')
    shelves = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]   
    product_index = column_names.index('product')
    amount_index = column_names.index('amount')
    capacity_index = column_names.index('capacity')
    price_index = column_names.index('price')
    x_index = column_names.index('x')
    y_index = column_names.index('y')
    for shelf in shelves:
        product_in_shelf = store_interface.store.get_product(shelf[product_index])
        s = Shelf(product = product_in_shelf, amount = shelf[amount_index], capacity = shelf[capacity_index])
        s.update_position(shelf[x_index], shelf[y_index])
        shelves_array.append(s)


    return shelves_array

def load_store_interface(interface_objects, cursor):
    store = load_store(cursor)

    money = get_money(cursor)
    market = load_market(interface_objects, money = money)

    return StoreInterface(store,market)

def load_store(cursor):
    products = load_products(cursor)

    store = Store(products)

    return store

def load_products(cursor):
    prod_array = []
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]   
    name_index = column_names.index('name')
    price_index = column_names.index('price')
    sell_price_index = column_names.index('sell_price')
    market_price_index = column_names.index('market_price')
    stock_index = column_names.index('stock')
    in_box_index = column_names.index('in_box')
    image_index = column_names.index('image')

    for product in products:
        p = Product(product[name_index], product[sell_price_index], product[image_index])
        p.price = product[price_index]
        p.market_price = product[market_price_index]
        p.stock = product[stock_index]
        p.in_box = product[in_box_index]

        prod_array.append(p)

    return prod_array

def get_money(cursor):
    cursor.execute('''SELECT * FROM supermarket''')
    supermarket = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]   
    money_index = column_names.index('money')

    supermarket = supermarket[0]

    money = supermarket[money_index]

    return money