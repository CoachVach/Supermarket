import sqlite3

from App.Classes.player import Player
from App.Classes.shelf import Shelf
from App.Helpers.Loading.new_game import load_cash_register, load_customers, load_store_interface
from App.Helpers.matrix_creation_helper import create_matrix
from App.Interfaces.Tablet.stock import StockInterface
from App.Interfaces.interface_objects import InterfaceObjects

def load_db(screen):
    conn = sqlite3.connect('game1.db')
    cursor = conn.cursor()

    interface_objects = InterfaceObjects(screen)
    store_interface = load_store_interface(interface_objects)
    interface_objects = load_interface_objects(interface_objects, cursor, store_interface)
    matrix = create_matrix(interface_objects.shelves)
    player = Player(matrix)
    customers = load_customers(matrix, store_interface.supermarket)
    stock_interface = StockInterface(store_interface.supermarket.stock)

    
    cursor.close()
    conn.close()

    return interface_objects, store_interface, matrix, player, customers, stock_interface


def xxx(conn, cursor):
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    for product in products:
        print(product)

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