import pygame
from utils.constants import Constants

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True
        self.fullscreen = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_button_down(event)

            elif self.model.current_mode != "menu" and event.type == pygame.KEYDOWN:
                self.handle_key_down(event)

    def handle_mouse_button_down(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.model.current_mode == "menu":
            self.handle_menu_mouse_click(mouse_pos)
        elif self.model.sidebar_open and mouse_pos[0] <= Constants.SIDEBAR_WIDTH:
            if event.button in (Constants.MOUSE_WHEEL_UP, Constants.MOUSE_WHEEL_DOWN):
                self.handle_sidebar_scroll(event.button)
            else:
                tile_index = self.model.get_tile_index_from_mouse_pos(mouse_pos)
                if tile_index is not None:
                    self.model.select_tile(tile_index)
        else:
            self.handle_canvas_click(mouse_pos, event.button)

    def handle_menu_mouse_click(self, mouse_pos):
        buttons = self.view.draw_menu(self.model.modes)
        for btn, mode_name in buttons:
            if btn.collidepoint(mouse_pos):
                self.model.change_mode(mode_name)
                return  # Early return to avoid unnecessary checks

    def handle_sidebar_click(self, mouse_pos, event):
        if event.button == Constants.MOUSE_WHEEL_UP:
            self.model.scroll_sidebar(-Constants.SCROLL_SPEED)
        elif event.button == Constants.MOUSE_WHEEL_DOWN:
            self.model.scroll_sidebar(Constants.SCROLL_SPEED)
        
        # Sidebar tile selection
        tile_index = self.model.get_tile_index_from_mouse_pos(mouse_pos)
        if tile_index is not None:
            self.model.select_tile(tile_index)
            
    def translate_to_grid_pos(self, mouse_pos):
        grid_x = mouse_pos[0] // (Constants.TILE_SIZE[0] * 3)
        grid_y = mouse_pos[1] // (Constants.TILE_SIZE[1] * 3)
        return (grid_x, grid_y)

    def handle_canvas_click(self, mouse_pos, button):
        grid_pos = self.translate_to_grid_pos(mouse_pos)
        
        if button == pygame.BUTTON_RIGHT and self.model.selected_tile_index is not None:
            self.model.paint_tile(grid_pos, self.model.selected_tile_index)
        elif button == pygame.BUTTON_LEFT:
            self.model.delete_tile(grid_pos)

    def translate_to_canvas_pos(self, mouse_pos):
        return mouse_pos  # Placeholder

    def handle_key_down(self, event):
        if event.key == Constants.KEY_TOGGLE_SIDEBAR:
            self.model.toggle_sidebar()
        elif event.key == Constants.KEY_TOGGLE_FULLSCREEN:
            self.toggle_fullscreen()

    def update_view(self):
        self.view.clear_screen()
        self.view.draw_canvas(self.model.canvas, self.model.tiles)  # Draw the canvas first
        if self.model.current_mode == "menu":
            self.view.draw_menu(self.model.modes)
        elif self.model.sidebar_open:
            self.view.draw_sidebar(self.model.tiles, self.model.sidebar_scroll_offset, self.model.selected_tile_index)
        pygame.display.flip()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.view.screen = pygame.display.set_mode(Constants.FULLSCREEN_MODE)
        else:
            self.view.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

    def run(self):
        while self.running:
            self.handle_events()
            self.update_view()
