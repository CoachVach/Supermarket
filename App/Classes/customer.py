import pygame, random

from App.Helpers.Constants.logic import CUSTOMER_VEL
from App.Helpers.Constants.interface import *
from App.Helpers.collision_helper import object_collision
from App.Helpers.Path_Finders.customer_path_finder import CustomerPathfinder
from App.Interfaces.Map.customer import CustomerInterface
from App.Interfaces.Messages.temp_message import TempMessage

from .purchase import Purchase

class Customer:

    def __init__(self, name, matrix, supermarket, money=0):
        self.name = name
        self.supermarket = supermarket
        self.interface = CustomerInterface()

        self.purchase = Purchase()

        self.path_finder = CustomerPathfinder(matrix, self)

        self.in_store = False
        self.waiting_cashier = False

        self.choosen_product = None
        self.choosen_shelf = None
        self.choosen_amount = 0

        self.speed = CUSTOMER_VEL
        self.pos = self.interface.position.rect().center
        self.direction = pygame.math.Vector2(0,0)
        self.path = []
        self.collision_rects = []
        self.empty_path = []

    def re_start(self):
        self.purchase = Purchase()

        self.in_store = False
        self.waiting_cashier = False

        self.choosen_product = None
        self.choosen_shelf = None
        self.choosen_amount = 0
        self.pos = self.interface.position.rect().center
        self.direction = pygame.math.Vector2(0,0)
        self.path = []
        self.collision_rects = []
        self.empty_path = []
    
    def add_product(self, interface_objects):
        if (self.choosen_shelf.amount >= self.choosen_amount) and (self.choosen_product == self.choosen_shelf.product):
            amount = self.purchase.add_product(self.choosen_product, self.choosen_amount)
            if amount == 0:
                interface_objects.temp_message = TempMessage("So Expensive!", (self.interface.position.x, self.interface.position.y), RED )
            self.choosen_shelf.remove_product(amount)

    def choose_product(self, products):
        product = random.choice(products)
        amount = random.randint(1, min(product.stock, 3))

        return product, amount
    
    def set_path(self, path, screen):
        self.path = path
        self.create_collision_rects(screen)
        self.get_direction()

    def create_collision_rects(self,screen):
        if self.path:
            self.collision_rects = []
            for point in self.path:
                x = (point.x * GRID_CELL_SIZE)
                y = (point.y * GRID_CELL_SIZE)
                rect = pygame.Rect((x,y),(GRID_CELL_SIZE,GRID_CELL_SIZE))
                self.collision_rects.append(rect)
                pygame.draw.rect(screen, BLUE, rect)

    def get_direction(self):
        if self.collision_rects:
            start = pygame.math.Vector2(self.pos)
            end = pygame.math.Vector2(self.collision_rects[0].center)
            self.direction = (end - start).normalize()
        else:
            self.direction = pygame.math.Vector2(0,0)
            self.path = []
    
    def check_collisions(self):
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(self.pos):
                    del self.collision_rects[0]
                    self.get_direction()
        else:
            self.path_finder.path = []

    def move(self, screen, interface_objects):
        if not self.waiting_cashier:
            self.pos += self.direction * self.speed
            self.check_collisions()
            self.interface.position.x = self.pos[0] - CUSTOMER_WIDTH/2
            self.interface.position.y = self.pos[1] - CUSTOMER_HEIGHT/2

            if self.in_store:
                if self.purchase.more_products_allowed():
                    self.handle_purchase(screen, interface_objects)
                else:
                    self.in_store = False
                    cash_register_pos = (interface_objects.cash_register.interface.position.x, interface_objects.cash_register.interface.position.y)
                    self.path_finder.create_path(cash_register_pos, screen)

            elif self.interface.position.rect().colliderect(interface_objects.cash_register.interface.position.rect()) and self.purchase != None:
                self.waiting_cashier = True

    def buy_purchase(self, interface_objects, screen):
        interface_objects.temp_message = self.supermarket.purchase(self.purchase)
        self.purchase = None
        leaving_pos = (LEAVING_X, LEAVING_Y)
        self.path_finder.create_path(leaving_pos, screen)
        self.waiting_cashier = False
            
    def handle_purchase(self, screen, interface_objects):
        products = self.get_buyable_products(interface_objects)

        if products != []:
            if self.choosen_product == None:
                self.choosen_product, self.choosen_amount = self.choose_product(products)

                self.choosen_shelf, shelf_position = interface_objects.shelf_position(self.choosen_product)

                self.path_finder.create_path_shelf(shelf_position, screen, interface_objects)

            elif self.interface.position.rect().colliderect(self.choosen_shelf.interface.position.rect()):
                self.add_product(interface_objects)

                self.choosen_product, self.choosen_shelf, self.choosen_amount = None, None, 0

        else:
            self.in_store = False
            cash_register_pos = (interface_objects.cash_register.interface.position.x, interface_objects.cash_register.interface.position.y)
            self.path_finder.create_path(cash_register_pos, screen)

    def get_buyable_products(self, interface_objects):
        products = interface_objects.products_in_shelfs()
        
        for product_tuple in self.purchase.products:
            for product in products:
                if product.name == product_tuple[0].name:
                    products.remove(product)
                    break

        return products

    def get_coord(self):
        col = self.interface.position.rect().centerx // GRID_CELL_SIZE
        row = self.interface.position.rect().centery // GRID_CELL_SIZE
        return (col,row)

    def draw(self, screen):
        self.interface.draw(screen)

    def __str__(self):
        return f"Customer: Name = {self.name}"