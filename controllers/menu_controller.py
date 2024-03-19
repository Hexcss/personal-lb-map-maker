import pygame

class MenuController:
    def __init__(self, menu, view, audio_controller):
        self.menu = menu
        self.view = view
        self.audio_controller = audio_controller

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.is_mouse_on_button(event.pos):
                    self.audio_controller.play_sound_effect('button_click')

    def update(self):
        pass
