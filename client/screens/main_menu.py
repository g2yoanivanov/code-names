"""Main menu screen for the Pygame client."""
import pygame

from client.screens import settings_menu
from settings import pygame_config
from client.components.button import ButtonBuilder


def main_menu(running: bool, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    Run the main menu screen.
    """
    pygame.display.set_caption("Main Menu")

    center = screen.get_rect().center

    join_button = (
        ButtonBuilder()
        .set_coords((center[0] - 100, center[1] - 100))
        .set_width(200)
        .set_height(50)
        .set_text("Join Game")
        .set_text_color(pygame_config.COLORS["CREAM"])
        .set_color(pygame_config.BTN_MAIN)
        .set_hover_color(pygame_config.BTN_HOVER)
        .set_shadow_color(pygame_config.BTN_SHADOW)
        .set_elevation(5)
        .build()
    )

    settings_button = (
            ButtonBuilder()
            .set_coords((center[0] - 100, center[1]))
            .set_width(200)
            .set_height(50)
            .set_text("Settings")
            .set_text_color(pygame_config.COLORS["CREAM"])
            .set_color(pygame_config.BTN_MAIN)
            .set_hover_color(pygame_config.BTN_HOVER)
            .set_shadow_color(pygame_config.BTN_SHADOW)
            .set_elevation(5)
            .build()
        )

    quit_button = (
        ButtonBuilder()
        .set_coords((center[0] - 100, center[1] + 100))
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

        if join_button.draw(screen):
            pass

        if settings_button.draw(screen):
            settings_menu.settings_menu(running, screen, clock)

        if quit_button.draw(screen):
            print("Quit button clicked!")
            running = False

        pygame.display.flip()
        clock.tick(pygame_config.FPS)

    pygame.quit()