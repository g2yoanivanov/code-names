import socket
import pygame

from settings import network_config, pygame_config
from .screens.main_menu import MainMenuScreen


def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((network_config.SERVER_IP, network_config.PORT))

    pygame.init()
    screen = pygame.display.set_mode(pygame_config.FULLSCREEN_SIZE, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    menu = MainMenuScreen(screen, clock)
    menu.run()

    pygame.quit()
    client.close()
