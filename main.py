import pygame
from views.menu_view import MenuView
from models.menu import Menu
from controllers.menu_controller import MenuController
from models.audio import AudioModel
from controllers.audio_controller import AudioController

class Application:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Lego Battles Map Editor")
        icon = pygame.image.load('assets/icons/icon.jpg')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.running = True
        self.views = ["menu", "map_editor"]
        self.current_view = "menu"

        self.audio_model = AudioModel()
        self.audio_controller = AudioController(self.audio_model)

        menu = Menu()
        menu_view = MenuView(menu, self.screen)
        self.menu_controller = MenuController(menu, menu_view, self.audio_controller)

        self.audio_model.load_sound_effect('button_click', 'assets/audio/sfx/button_sfx.wav')
        self.audio_model.load_music_track('main_menu', 'assets/audio/music/main_menu.wav')

        self.audio_controller.play_music('main_menu')

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if self.current_view == "menu":
                    self.menu_controller.handle_events(events)

            self.screen.fill((0, 0, 0))  # Clear screen
            self.menu_controller.view.draw()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    app = Application()
    app.run()
