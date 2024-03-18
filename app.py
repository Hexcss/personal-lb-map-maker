import pygame
from game_controller import GameController
from game_model import GameModel
from game_view import GameView

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Lego Battles Map Editor")
    model = GameModel()
    view = GameView(screen)
    controller = GameController(model, view)
    controller.run()
    pygame.quit()

if __name__ == "__main__":
    main()
