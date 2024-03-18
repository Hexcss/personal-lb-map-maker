import pygame
from utils.constants import Constants

class GameView:
    def __init__(self, screen):
        self.screen = screen

    def draw_menu(self, menu_data):
        font = pygame.font.Font(None, Constants.FONT_SIZE)
        buttons = []
        for i, (text, _) in enumerate(menu_data.items()):
            text_surface = font.render(text, True, Constants.TEXT_COLOR)
            x = Constants.MENU_BUTTON_MARGIN
            y = Constants.MENU_BUTTON_MARGIN + i * Constants.MENU_BUTTON_SPACING
            self.screen.blit(text_surface, (x, y))
            buttons.append((pygame.Rect(x, y, text_surface.get_width(), text_surface.get_height()), text))
        return buttons

    def draw_action_buttons(self):
        font = pygame.font.Font(None, Constants.FONT_SIZE)
        text_surface = font.render("Back to Menu", True, Constants.TEXT_COLOR)
        x = (Constants.SIDEBAR_WIDTH - text_surface.get_width()) // 2
        y = (Constants.ACTIONS_HEIGHT - text_surface.get_height()) // 2
        self.screen.blit(text_surface, (x, y))
        back_button_rect = pygame.Rect(x, y, text_surface.get_width(), text_surface.get_height())

        pygame.draw.rect(self.screen, Constants.ACTION_AREA_COLOR, pygame.Rect(0, 0, Constants.SIDEBAR_WIDTH, Constants.ACTIONS_HEIGHT))
        pygame.draw.line(self.screen, Constants.LINE_COLOR, (0, Constants.ACTIONS_HEIGHT), (Constants.SIDEBAR_WIDTH, Constants.ACTIONS_HEIGHT))

        return back_button_rect
    
    def draw_grid(self):
        for x in range(0, self.screen.get_width(), Constants.TILE_SIZE[0] * 3):
            pygame.draw.line(self.screen, Constants.GRID_COLOR, (x, 0), (x, self.screen.get_height()))
        for y in range(0, self.screen.get_height(), Constants.TILE_SIZE[1] * 3):
            pygame.draw.line(self.screen, Constants.GRID_COLOR, (0, y), (self.screen.get_width(), y))

    def draw_canvas(self, canvas, tiles):
        self.draw_grid()    
        for position, tile_index in canvas.items():
            screen_x, screen_y = position[0] * Constants.TILE_SIZE[0] * 3, position[1] * Constants.TILE_SIZE[1] * 3
            tile = tiles[tile_index]
            scaled_tile = pygame.transform.scale(tile, (Constants.TILE_SIZE[0] * 3, Constants.TILE_SIZE[1] * 3))
            self.screen.blit(scaled_tile, (screen_x, screen_y))

    def calculate_screen_position_from_canvas_pos(self, position):
        # Implement based on your canvas setup
        return position[0], position[1]  # Placeholder


    def draw_sidebar(self, tiles, scroll_offset=0, selected_tile_index=None):
        tile_size = (Constants.TILE_SIZE[0] * 3, Constants.TILE_SIZE[1] * 3)
        padding = Constants.TILE_PADDING
        actions_height = Constants.ACTIONS_HEIGHT

        pygame.draw.rect(self.screen, Constants.SIDEBAR_COLOR, pygame.Rect(0, 0, Constants.SIDEBAR_WIDTH, Constants.SCREEN_HEIGHT))

        back_button_rect = self.draw_action_buttons()

        columns = Constants.SIDEBAR_WIDTH // (tile_size[0] + padding)
        
        y_start = actions_height + padding
        
        for i, tile in enumerate(tiles):
            scaled_tile = pygame.transform.scale(tile, tile_size)
            col = i % columns
            row = i // columns
            x = col * (tile_size[0] + padding)
            
            y = y_start + row * (tile_size[1] + padding) - scroll_offset

            if y >= y_start:
                self.screen.blit(scaled_tile, (x, y))
                
        if selected_tile_index is not None:
            selected_tile_row = selected_tile_index // columns
            selected_tile_col = selected_tile_index % columns
            selected_x = selected_tile_col * (tile_size[0] + padding)
            selected_y = y_start + selected_tile_row * (tile_size[1] + padding) - scroll_offset
            
            if y_start <= selected_y < Constants.SIDEBAR_HEIGHT:
                pygame.draw.rect(
                    self.screen,
                    Constants.SELECTED_TILE_COLOR,
                    (selected_x, selected_y, tile_size[0], tile_size[1]),
                    2  # Width of the border
                )


        return back_button_rect

    def clear_screen(self):
        self.screen.fill((0, 0, 0))