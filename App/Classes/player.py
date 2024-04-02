import pygame

from App.Helpers.collision_helper import object_collision
from App.Helpers.Path_Finders.path_finder import Pathfinder
from .position import Position

from ..Helpers.Constants.logic import *
from ..Helpers.Constants.interface import *

class Player:

    def __init__(self, matrix,  name="Erik", carrying_product=None):
        self.name = name
        self.position = Position(width=PLAYER_WIDTH,height=PLAYER_HEIGHT)
        self.carrying_product = carrying_product
        self.carrying_amount = 0
        self.capacity = PLAYER_CAPACITY

        self.path_finder = Pathfinder(matrix, self)

        self.image = pygame.transform.scale(pygame.image.load("Images/player.png").convert_alpha(), (self.position.width, self.position.height))

        self.speed = PLAYER_VEL
        self.pos = self.position.rect().center
        self.direction = pygame.math.Vector2(0,0)
        self.path = []
        self.collision_rects = []
        self.empty_path = []

    def get_product(self, boxes):
        boxes = object_collision(boxes, self.augmented_rect())

        if boxes != []:
            box = boxes[0]
            self.carrying_product, self.carrying_amount = box.get_product(self.capacity)
            self.carrying_product.in_box -= self.carrying_amount

    def re_stock(self, shelves):
        shelves = object_collision(shelves, self.augmented_rect())

        for shelf in shelves:

            if shelf.add_product(self.carrying_product):

                self.carrying_amount -= 1
                if self.carrying_amount == 0:
                    self.carrying_product = None

                break

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

    def move(self):
        self.pos += self.direction * self.speed
        self.check_collisions()
        self.position.x = self.pos[0] - PLAYER_WIDTH/2
        self.position.y = self.pos[1] - PLAYER_HEIGHT/2
    
    def cash_register(self, customers, interface_objects, screen):
        position_rect = self.position.rect()
        register_rect = interface_objects.cash_register.interface.position.rect()
        if position_rect.colliderect(register_rect):
            for customer in customers:
                if customer.waiting_cashier:
                    if position_rect.colliderect(register_rect):
                        customer.buy_purchase(interface_objects, screen)
                        pygame.mixer.music.load(interface_objects.cash_register.sound)
                        pygame.mixer.music.play()
                        break

    def get_coord(self):
        col = self.position.rect().centerx // GRID_CELL_SIZE
        row = self.position.rect().centery // GRID_CELL_SIZE
        return (col,row)

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
        product_position = Position(self.position.x, self.position.y, SHELF_WIDTH / 3, SHELF_HEIGHT / 2)
        if self.carrying_product != None:
            self.carrying_product.draw(screen, product_position)

    def augmented_rect(self):
        augmented_pos = Position(self.position.x-PLAYER_AUGMENTATION, self.position.y - PLAYER_AUGMENTATION, self.position.width + 2*PLAYER_AUGMENTATION, self.position.height + 2*PLAYER_AUGMENTATION)
        return augmented_pos.rect()