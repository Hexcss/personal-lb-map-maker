import pygame

class Constants:
    # Screen dimensions
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    
    GRID_COLOR = (100, 100, 100)

    # Fullscreen mode
    FULLSCREEN_MODE = (0, 0), pygame.FULLSCREEN

    # Sidebar dimensions and properties
    SIDEBAR_WIDTH = 200
    SIDEBAR_HEIGHT = SCREEN_HEIGHT
    ACTIONS_HEIGHT = 50
    TILE_SIZE = (8, 8)
    TILE_PADDING = 3
    SCROLL_SPEED = 20

    # Colors
    ACTION_AREA_COLOR = (180, 180, 180)
    SIDEBAR_COLOR = (200, 200, 200)
    LINE_COLOR = (0, 0, 0)
    TEXT_COLOR = (255, 255, 255)
    BACKGROUND_COLOR = (0, 0, 0)  # Assuming a black background

    # Font properties
    FONT_SIZE = 36
    FONT_PATH = None  # Use Pygame's default font

    # Menu button properties
    MENU_BUTTON_MARGIN = 50
    MENU_BUTTON_SPACING = 50

    # Mode file paths
    MODES = {
        "CASTLE": "assets/tiles/castle/tiles.png",
        "PIRATE": "assets/tiles/pirates/tiles.png",
        "SPACE": "assets/tiles/space/tiles.png"
    }

    # Mouse wheel
    MOUSE_WHEEL_UP = 4
    MOUSE_WHEEL_DOWN = 5

    # Keys
    KEY_TOGGLE_SIDEBAR = pygame.K_TAB
    KEY_TOGGLE_FULLSCREEN = pygame.K_F11

    SELECTED_TILE_COLOR = (255, 255, 0) 