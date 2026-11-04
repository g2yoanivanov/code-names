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

    center = screen.get_rect().center

    start_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2,
            center[1] - 2*pygame_config.BTN_SPACING
        ))
        .set_text("Start Game")
        .build()
    )

    fullscreen_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2,
            center[1] - pygame_config.BTN_SPACING
        ))
        .set_text("Fullscreen")
        .build()
    )

    windowed_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2,
            center[1]
        ))
        .set_text("800x600")
        .build()
    )

    back_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2,
            center[1] + 2*pygame_config.BTN_SPACING
        ))
        .set_text("Done")
        .build()
    )

    while running:
        screen.fill(pygame_config.BG_MAIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if fullscreen_button.draw(screen):
            pass

        if windowed_button.draw(screen):
            pass

        if start_button.draw(screen):
            main_menu.main_menu(running, screen, clock)

        if back_button.draw(screen):
            print("Back button clicked!")
            running = False

        pygame.display.flip()
        clock.tick(pygame_config.FPS)
