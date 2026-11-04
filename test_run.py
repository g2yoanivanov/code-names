import pygame

from client.screens import main_menu
from settings import pygame_config


def main() -> None:
    """
    Entry point for the application.
    """
    pygame.init()
    screen = pygame.display.set_mode(pygame_config.FULLSCREEN_SIZE, pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    running = True

    main_menu.main_menu(running, screen, clock)

    pygame.quit()

if __name__ == "__main__":
    main()