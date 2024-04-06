import sqlite3

def save_db(interface_objects, store_interface, customers, stock_interface):
    conn = sqlite3.connect('game1.db')
    cursor = conn.cursor()

    save_products(conn, cursor, store_interface)

    save_shelves(conn, cursor, interface_objects)

    save_stock(conn, cursor, stock_interface)

    save_money(conn, cursor, store_interface)

    cursor.close()
    conn.close()

def save_products(conn, cursor, store_interface):
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        price REAL,
                        sell_price REAL,
                        market_price REAL,
                        stock INTEGER,
                        in_box INTEGER
                    )''')
    products_data = store_interface.store.products_data()

    cursor.executemany('''INSERT OR IGNORE INTO products (name, price, sell_price, market_price, stock, in_box) 
                            VALUES (?, ?, ?, ?, ?, ?)''', products_data)
    conn.commit()

    """
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    print("Products in the database:")
    for product in products:
        print(product)

    """

def save_shelves(conn, cursor, inteface_objects):
    cursor.execute('''CREATE TABLE IF NOT EXISTS shelves (
                        id INTEGER PRIMARY KEY,
                        product TEXT NOT NULL,
                        amount INTEGER,
                        capacity INTEGER,
                        price REAL,
                        x INTEGER,
                        y INTEGER
                    )''')
    data = inteface_objects.shelf_data()

    cursor.executemany('''INSERT OR IGNORE INTO shelves (product, amount, capacity, price, x, y) 
                            VALUES (?, ?, ?, ?, ?, ?)''', data)
    conn.commit()

    """
    cursor.execute('''SELECT * FROM shelves''')
    shelves = cursor.fetchall()
    print("Shelves in the database:")
    for shelf in shelves:
        print(shelf)
    """

def save_stock(conn, cursor, stock_interface):
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock (
                        id INTEGER PRIMARY KEY,
                        product TEXT NOT NULL, 
                        price REAL
                    )''')
    data = stock_interface.stock.data()

    print(data)

    cursor.executemany('''INSERT OR IGNORE INTO stock (product, price) 
                            VALUES (?, ?)''', data)
    conn.commit()

    """
    cursor.execute('''SELECT * FROM stock''')
    stock = cursor.fetchall()
    print("Stock in the database:")
    for s in stock:
        print(s)
    """

def save_money(conn, cursor, store_interface):
    cursor.execute('''CREATE TABLE IF NOT EXISTS supermarket (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL, 
                        money REAL
                    )''')
    money = store_interface.supermarket.money

    data =[("Supermarket", money)]

    cursor.executemany('''INSERT OR IGNORE INTO supermarket (name, money) 
                            VALUES (?, ?)''', data)
    conn.commit()

    
    cursor.execute('''SELECT * FROM supermarket''')
    supermarket = cursor.fetchall()
    print("supermarket in the database:")
    for s in supermarket:
        print(s)
    