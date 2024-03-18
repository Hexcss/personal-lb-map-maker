import pygame
from utils.constants import Constants

class GameModel:
    def __init__(self):
        self.modes = Constants.MODES
        self.current_mode = "menu"
        self.tiles = []
        self.sidebar_open = False
        self.sidebar_scroll_offset = 0
        self.selected_tile_index = None
        self.canvas = {}

    def load_tileset(self, path):
        tile_size = Constants.TILE_SIZE
        tileset = pygame.image.load(path).convert_alpha()
        tile_width, tile_height = tile_size
        image_width, image_height = tileset.get_size()
        tiles = []
        for y in range(0, image_height, tile_height):
            for x in range(0, image_width, tile_width):
                rect = pygame.Rect(x, y, tile_width, tile_height)
                tile = tileset.subsurface(rect)
                tiles.append(tile)
        return tiles

    def change_mode(self, mode):
        self.current_mode = mode
        if mode in self.modes:
            self.tiles = self.load_tileset(self.modes[mode])
            
    def scroll_sidebar(self, amount):
        tile_size = (Constants.TILE_SIZE[0] * 3, Constants.TILE_SIZE[1] * 3)
        padding = Constants.TILE_PADDING
        sidebar_height = Constants.SIDEBAR_HEIGHT
        actions_height = Constants.ACTIONS_HEIGHT

        self.sidebar_scroll_offset += amount

        columns = Constants.SIDEBAR_WIDTH // (tile_size[0] + padding)
        rows = (len(self.tiles) + columns - 1) // columns  

        total_tiles_height = rows * (tile_size[1] + padding) + actions_height
        max_offset = max(total_tiles_height - sidebar_height, 0)

        self.sidebar_scroll_offset = max(0, min(self.sidebar_scroll_offset, max_offset))

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open
        
    def select_tile(self, index):
        if 0 <= index < len(self.tiles):
            self.selected_tile_index = index
            
    def paint_tile(self, grid_pos, tile_index):
        self.canvas[grid_pos] = tile_index

    def delete_tile(self, grid_pos):
        if grid_pos in self.canvas:
            del self.canvas[grid_pos]
            
    def get_tile_index_from_mouse_pos(self, mouse_pos):
        if not self.sidebar_open:
            return None 
        
        local_x = mouse_pos[0]
        local_y = mouse_pos[1] - Constants.ACTIONS_HEIGHT + self.sidebar_scroll_offset
        
        col = local_x // (Constants.TILE_SIZE[0] * 3 + Constants.TILE_PADDING)
        row = local_y // (Constants.TILE_SIZE[1] * 3 + Constants.TILE_PADDING)
        
        index = row * (Constants.SIDEBAR_WIDTH // (Constants.TILE_SIZE[0] * 3 + Constants.TILE_PADDING)) + col
        
        if 0 <= index < len(self.tiles):
            return index
        else:
            return None  
            
    