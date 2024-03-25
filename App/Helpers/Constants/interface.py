GAME_TITLE = "Supermarket"

#SCREEN
SCREEN_WIDTH = 832
SCREEN_HEIGHT = 624

#IMG
IMAGE_PATH = "Images/Products/"

#COLORS:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GRAY = (200, 200, 200)
DARK_GRAY = (75, 75, 75)

RED_GRAY = (255, 150, 150)

#MAP
MAP_OFFSET = 50

#GRID
GRID_CELL_SIZE = 26

#CUSTOMER
CUSTOMER_COLOR = RED_GRAY
CUSTOMER_WIDTH = GRID_CELL_SIZE
CUSTOMER_HEIGHT = GRID_CELL_SIZE

#PLAYER
PLAYER_WIDTH = GRID_CELL_SIZE
PLAYER_HEIGHT = 2*GRID_CELL_SIZE

#TABLET
TABLET_OFFSET = 100
TABLET_WIDTH = SCREEN_WIDTH - 2*TABLET_OFFSET
TABLET_HEIGHT = SCREEN_HEIGHT - 2*TABLET_OFFSET

#PRODUCT IN TABLET
PRODUCT_OFFSET = 10
PRODUCT_WIDTH = (TABLET_WIDTH - (6*PRODUCT_OFFSET) ) / 3
PRODUCT_HEIGHT = (TABLET_HEIGHT - (6*PRODUCT_OFFSET) ) / 3

#BUTTON
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 100
BUTTON_Y = TABLET_OFFSET + TABLET_HEIGHT/2 - BUTTON_HEIGHT/2
BUTTON_OFFSET = (TABLET_WIDTH - 2*BUTTON_WIDTH) / 3

#EXIT
EXIT_BUTTON_WIDTH = 36
EXIT_BUTTON_HEIGHT = 36

#SHELF
SHELF_HEIGHT = 2*GRID_CELL_SIZE
SHELF_WIDTH = 4*GRID_CELL_SIZE

#BOX
BOX_WIDTH = 50
BOX_HEIGHT = 50
BOX_COLOR = GREEN

#ADD SHELF BUTTON
ADD_SHELF_BUTTON_X = SCREEN_WIDTH - 200 
ADD_SHELF_BUTTON_Y = SCREEN_HEIGHT - 200
ADD_SHELF_BUTTON_WIDTH = 130
ADD_SHELF_BUTTON_HEIGHT = 40

#TEXT
FONT_SIZE = 36
TEXT_OFFSET = 6