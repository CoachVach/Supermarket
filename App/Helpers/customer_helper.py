import random


def random_customer(customers, interface_objects):
    not_buying_customers = []
    for customer in customers:
        if not customer.in_store and not customer.waiting_cashier and customer.path == [] and interface_objects.products_in_shelfs() != []:
            not_buying_customers.append(customer)
    if not_buying_customers != []:
        customer = random.choice(not_buying_customers)
        customer.re_start()
        customer.in_store = True