"""Settings menu screen for the Pygame client."""
import pygame

from settings import pygame_config
from client.components.button import ButtonBuilder

from . import main_menu


def settings_menu(running: bool, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    Run the settings menu screen.
    """
    pygame.display.set_caption("Settings Menu")

    start_button = (
        ButtonBuilder()
        .set_coords((300, 200))
        .set_width(200)
        .set_height(50)
        .set_text("Start Game")
        .set_text_color(pygame_config.COLORS["CREAM"])
        .set_color(pygame_config.BTN_MAIN)
        .set_hover_color(pygame_config.BTN_HOVER)
        .set_shadow_color(pygame_config.BTN_SHADOW)
        .set_elevation(5)
        .build()
    )

    fullscreen_button = (
        ButtonBuilder()
        .set_coords((300, 300))
        .set_width(200)
        .set_height(50)
        .set_text("Fullscreen")
        .set_text_color(pygame_config.COLORS["CREAM"])
        .set_color(pygame_config.BTN_MAIN)
        .set_hover_color(pygame_config.BTN_HOVER)
        .set_shadow_color(pygame_config.BTN_SHADOW)
        .set_elevation(5)
        .build()
    )

    windowed_button = (
        ButtonBuilder()
        .set_coords((300, 400))
        .set_width(200)
        .set_height(50)
        .set_text("800x600")
        .set_text_color(pygame_config.COLORS["CREAM"])
        .set_color(pygame_config.BTN_MAIN)
        .set_hover_color(pygame_config.BTN_HOVER)
        .set_shadow_color(pygame_config.BTN_SHADOW)
        .set_elevation(5)
        .build()
    )

    quit_button = (
        ButtonBuilder()
        .set_coords((300, 500))
        .set_width(200)
        .set_height(50)
        .set_text("Quit")
        .set_text_color(pygame_config.COLORS["CREAM"])
        .set_color(pygame_config.BTN_MAIN)
        .set_hover_color(pygame_config.BTN_HOVER)
        .set_shadow_color(pygame_config.BTN_SHADOW)
        .set_elevation(5)
        .build()
    )

    while running:
        screen.fill(pygame_config.BG_MAIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if fullscreen_button.draw(screen):
            screen = pygame.display.set_mode(
                pygame_config.FULLSCREEN_SIZE,
                pygame.FULLSCREEN
            )

        if windowed_button.draw(screen):
            screen = pygame.display.set_mode(
                pygame_config.SCREEN_SIZE
            )

        if start_button.draw(screen):
            main_menu.main_menu(running, screen, clock)

        if quit_button.draw(screen):
            print("Quit button clicked!")
            running = False

        pygame.display.flip()
        clock.tick(pygame_config.FPS)

    pygame.quit()
    pygame.quit()