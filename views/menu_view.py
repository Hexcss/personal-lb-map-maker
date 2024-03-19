import pygame

class MenuView:
    def __init__(self, menu, screen):
        self.menu = menu
        self.screen = screen
        background_image = pygame.image.load('assets/menu/background.png')
        self.background_image = pygame.transform.scale(background_image, screen.get_size())
        self.font = pygame.font.Font('assets/fonts/font_2.ttf', 36)
        self.title_font = pygame.font.Font('assets/fonts/font_2.ttf', 72)
        self.button_color = (20, 50, 100)  
        self.button_hover_color = (40, 100, 200)  
        self.text_color = (255, 255, 255)
        self.button_border_color = (255, 255, 255)
        self.button_border_width = 2
        self.line_spacing = 10
        self.button_width = 200
        self.button_height = 50
        self.button_gap = 20

    def draw_button(self, text, position, size, mouse_pos):
        button_rect = pygame.Rect(position, size)
        
        button_background_color = self.button_color if button_rect.collidepoint(mouse_pos) else self.button_hover_color
        pygame.draw.rect(self.screen, button_background_color, button_rect)
        
        
        border_radius = 5  
        pygame.draw.rect(self.screen, self.button_border_color, button_rect, self.button_border_width, border_radius)

        text_surf = self.font.render(text, True, self.text_color)
        text_rect = text_surf.get_rect(center=button_rect.center)
        
        blitted_rect = self.screen.blit(text_surf, text_rect)
        
        return blitted_rect
        
    def draw_title(self, title_lines):
        total_title_height = sum(self.title_font.size(line)[1] + self.line_spacing for line in title_lines)
        y_offset = (self.screen.get_height() - total_title_height) / 2 - 200  
        
        shadow_color = (0, 0, 0)
        shadow_offset = (2, 2) 

        for line in title_lines:
            title_surf = self.title_font.render(line, True, self.text_color)
            title_rect = title_surf.get_rect(center=(self.screen.get_width() // 2, y_offset))
            shadow_rect = title_surf.get_rect(center=(self.screen.get_width() // 2 + shadow_offset[0], y_offset + shadow_offset[1]))

            self.screen.blit(title_surf, shadow_rect, special_flags=pygame.BLEND_RGBA_MULT)

            self.screen.blit(title_surf, title_rect)

            y_offset += title_surf.get_height() + self.line_spacing
            
    def is_mouse_on_button(self, mouse_pos):
        for button_rect in self.button_rects:
            if button_rect.collidepoint(mouse_pos):
                return True
        return False
    
    def get_button_position(self, index):
        start_y = (self.screen.get_height() - (self.button_height + self.button_gap) * len(self.menu.items) - self.button_gap) // 2
        return ((self.screen.get_width() - self.button_width) // 2, start_y + index * (self.button_height + self.button_gap))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        title_lines = ["Lego Battles", "Map Editor"]
        self.draw_title(title_lines)  
        
        mouse_pos = pygame.mouse.get_pos() 
        self.button_rects = [] 
        
        total_height = (self.button_height + self.button_gap) * len(self.menu.items) - self.button_gap
        start_y = (self.screen.get_height() - total_height) // 2

        for i, item in enumerate(self.menu.items):
            position = ((self.screen.get_width() - self.button_width) // 2, start_y + i * (self.button_height + self.button_gap))

            button_rect = self.draw_button(item, position, (self.button_width, self.button_height), mouse_pos)
            self.button_rects.append(button_rect)
            