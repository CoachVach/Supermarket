import pygame
from .position import Position

from ..Helpers.Constants.logic import *
from ..Helpers.Constants.interface import *


class Player:

    def __init__(self, name="Erik", carrying_product=None):
        self.name = name
        self.position = Position(width=20,height=50)
        self.carrying_product = carrying_product
        self.carrying_amount = 0
        self.capacity = PLAYER_CAPACITY

    def get_product(self, boxes):
        boxes = self.object_collision(boxes, self.augmented_rect())

        if boxes != []:
            box = boxes[0]
            self.carrying_product, self.carrying_amount = box.get_product(self.capacity)

    def re_stock(self, shelves):
        shelves = self.object_collision(shelves, self.augmented_rect())

        for shelf in shelves:

            if shelf.add_product(self.carrying_product):

                self.carrying_amount -= 1
                if self.carrying_amount == 0:
                    self.carrying_product = None

                break
        
    def move_left(self, shelves):
        if self.position.x >= MAP_OFFSET:
            self.position.x -= PLAYER_VEL
            if self.object_collision(shelves, self.position.rect()) != []:
                self.position.x += PLAYER_VEL

    def move_right(self, shelves):
        if self.position.x + self.position.width <= SCREEN_WIDTH - MAP_OFFSET:
            self.position.x += PLAYER_VEL
            if self.object_collision(shelves, self.position.rect()) != []:
                self.position.x -= PLAYER_VEL

    def move_up(self, shelves):
        if self.position.y >= MAP_OFFSET:
            self.position.y -= PLAYER_VEL
            if self.object_collision(shelves, self.position.rect()) != []:
                self.position.y += PLAYER_VEL

    def move_down(self, shelves):
        if self.position.y + self.position.height <= SCREEN_HEIGHT - MAP_OFFSET:
            self.position.y += PLAYER_VEL
            if self.object_collision(shelves, self.position.rect()) != []:
                self.position.y -= PLAYER_VEL

    def move(self, shelves):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move_left(shelves)
        if keys[pygame.K_RIGHT]:
            self.move_right(shelves)
        if keys[pygame.K_UP]:
            self.move_up(shelves)
        if keys[pygame.K_DOWN]:
            self.move_down(shelves)

    def object_collision(self, objects, rect):
        collisions = []
        for object in objects:
            if object.interface.rect().colliderect(rect):
                collisions.append(object)
        return collisions

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position.x, self.position.y, self.position.width, self.position.height))
        product_position = Position(self.position.x, self.position.y, SHELF_WIDTH / 3, SHELF_HEIGHT / 2)
        if self.carrying_product != None:
            self.carrying_product.draw(screen, product_position)

    def augmented_rect(self):
        augmented_pos = Position(self.position.x-PLAYER_AUGMENTATION, self.position.y - PLAYER_AUGMENTATION, self.position.width + 2*PLAYER_AUGMENTATION, self.position.height + 2*PLAYER_AUGMENTATION)
        return augmented_pos.rect()