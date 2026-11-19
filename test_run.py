import pygame

from client.screens.main_menu import MainMenuScreen
from settings import pygame_config


def main() -> None:
    """
    Entry point for testing the UI screens.
    """
    pygame.init()
    screen = pygame.display.set_mode(pygame_config.FULLSCREEN_SIZE, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    menu = MainMenuScreen(screen, clock)
    menu.run()

    pygame.quit()


if __name__ == "__main__":
    main()
