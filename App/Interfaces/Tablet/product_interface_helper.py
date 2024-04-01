import pygame

from App.Helpers.Constants.interface import *
from App.Helpers.interface_tools import *

def draw_product(product, screen, button_clicked, mouse_pos, i, market, interface_objects):
    x, y = product_position(i)

    rect = pygame.Rect(x, y, PRODUCT_WIDTH, PRODUCT_HEIGHT)

    minus_rect, plus_rect = get_amount_selection_rects(x,y)

    color = BLACK
    can_buy = market.supermarket.can_buy(product)
    if not can_buy:
        color = DARK_GRAY
    minus_color = RED
    plus_color = RED

    if minus_rect.collidepoint(mouse_pos):
        minus_color = GRAY
        if button_clicked:
            product.decrement_selection()

    elif plus_rect.collidepoint(mouse_pos):
        plus_color = GRAY
        if button_clicked:
            product.increment_selection()
            
    elif rect.collidepoint(mouse_pos):
        if button_clicked:
            _,interface_objects.temp_message = market.buy_product(product)
            
        if can_buy:
            color = GREEN
        else:
            color = RED


    pygame.draw.rect(screen, color, rect)

    draw_amount_selection(screen, x, y, minus_rect, plus_rect, minus_color, plus_color, product.selection)
    
    display_text(screen, f"{product.name}", WHITE, (x,y))
    display_text(screen, f"${product.sell_price}", WHITE, (x,y + FONT_SIZE))

def draw_product_in_stock(product, screen, button_clicked, mouse_pos, i):
    x, y = product_position(i)

    rect = pygame.Rect(x, y, PRODUCT_WIDTH, PRODUCT_HEIGHT)

    minus_rect, plus_rect = minus_rect_stock(x,y), plus_rect_stock(x,y)

    color = BLACK
    minus_color = RED
    plus_color = RED

    if minus_rect.collidepoint(mouse_pos):
        minus_color = GRAY
        if button_clicked:
            product.decrement_price()

    elif plus_rect.collidepoint(mouse_pos):
        plus_color = GRAY
        if button_clicked:
            product.increment_price()

    pygame.draw.rect(screen, color, rect)

    draw_amount_selection_stock(screen, x, y, minus_rect, plus_rect, minus_color, plus_color, product.price)
    
    draw_quantity(screen, x, y, product)

    display_text(screen, f"{product.name}", WHITE, (x,y))
    display_text(screen, f"Cost: ${product.sell_price}", WHITE, (x,y + 25))
    display_text(screen, f"Market: ${product.market_price}", WHITE, (x,y + 50))
    display_profit(screen, x, y, product)

def product_position(i):
    column = i % 3
    row = i // 3

    offset_x = TABLET_OFFSET + (column + 2)*PRODUCT_OFFSET
    previous_products_x = column*PRODUCT_WIDTH

    offset_y = TABLET_OFFSET + (row + 2)*PRODUCT_OFFSET
    previous_products_y = row*PRODUCT_HEIGHT

    return offset_x + previous_products_x, offset_y + previous_products_y

def get_amount_selection_rects(x, y):
    return minus_rect(x, y), plus_rect(x, y)

def minus_rect(x, y):
    button_x = x + PRODUCT_WIDTH/2 - FONT_SIZE
    button_y = y + PRODUCT_HEIGHT/2 
    button_width = FONT_SIZE
    button_height = FONT_SIZE

    rect = pygame.Rect(button_x, button_y, button_width, button_height)

    return rect

def plus_rect(x, y):
    button_x = x + PRODUCT_WIDTH/2 + FONT_SIZE
    button_y = y + PRODUCT_HEIGHT/2 
    button_width = FONT_SIZE
    button_height = FONT_SIZE

    rect = pygame.Rect(button_x, button_y, button_width, button_height)

    return rect

def draw_amount_selection(screen, x, y, minus_rect, plus_rect, minus_color, plus_color, selection):
    draw_button(screen, minus_rect, minus_color, "-")

    draw_amount(screen, x, y, str(selection))

    draw_button(screen, plus_rect, plus_color, "+")

def draw_button(screen, rect, color, text):

    pygame.draw.rect(screen, color, rect)

    display_text(screen, text, WHITE, (rect.x + TEXT_OFFSET, rect.y + TEXT_OFFSET))

def draw_amount(screen, x, y, amount):
    number_x = x + PRODUCT_WIDTH/2 
    number_y = y + PRODUCT_HEIGHT/2 

    display_text(screen, amount, WHITE, (number_x + TEXT_OFFSET,number_y + TEXT_OFFSET))

def minus_rect_stock(x, y):
    button_x = x
    button_y = y + PRODUCT_HEIGHT/2 + 15
    button_width = FONT_SIZE
    button_height = FONT_SIZE

    rect = pygame.Rect(button_x, button_y, button_width, button_height)

    return rect

def plus_rect_stock(x, y):
    button_x = x + PRODUCT_WIDTH/2 + FONT_SIZE - 25
    button_y = y + PRODUCT_HEIGHT/2 + 15
    button_width = FONT_SIZE
    button_height = FONT_SIZE

    rect = pygame.Rect(button_x, button_y, button_width, button_height)

    return rect

def draw_amount_selection_stock(screen, x, y, minus_rect, plus_rect, minus_color, plus_color, selection):
    draw_button(screen, minus_rect, minus_color, "-")

    draw_amount_stock(screen, x, y, str("{:.2f}".format(selection)))

    draw_button(screen, plus_rect, plus_color, "+")

def draw_amount_stock(screen, x, y, amount):
    number_x = x + FONT_SIZE
    number_y = y + PRODUCT_HEIGHT/2 + 15

    display_text(screen, amount, WHITE, (number_x + TEXT_OFFSET,number_y + TEXT_OFFSET))

def display_profit(screen, x, y, product):
    profit = "{:.2f}".format(product.price - product.sell_price)
    profit_color = GREEN if (product.price - product.sell_price) >= 0 else RED
    display_custom_text(screen, profit, 25, profit_color, (x + PRODUCT_WIDTH - 40,y + PRODUCT_HEIGHT/2 + 25))

def draw_quantity(screen, x, y, product):
    rect = pygame.Rect(x + PRODUCT_WIDTH - FONT_SIZE, y, FONT_SIZE, 30)

    pygame.draw.rect(screen, WHITE, rect)

    display_text(screen, str(product.stock), BLACK, (x + PRODUCT_WIDTH - FONT_SIZE + 5, y))