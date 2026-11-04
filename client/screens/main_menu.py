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

    host_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2,
            center[1] - 2*pygame_config.BTN_SPACING
        ))
        .set_text("Host Game")
        .build()
    )

    join_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2, 
            center[1] - pygame_config.BTN_SPACING
        ))
        .set_text("Join Game")
        .build()
    )

    settings_button = (
            ButtonBuilder()
            .set_coords((
                center[0] - pygame_config.BTN_WIDTH // 2, 
                center[1]
            ))
            .set_text("Settings")
            .build()
        )

    quit_button = (
        ButtonBuilder()
        .set_coords((
            center[0] - pygame_config.BTN_WIDTH // 2,
            center[1] + pygame_config.BTN_SPACING
        ))
        .set_text("Quit")
        .build()
    )

    while running:
        screen.fill(pygame_config.BG_MAIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if host_button.draw(screen):
            pass

        if join_button.draw(screen):
            pass

        # if settings_button.draw(screen):
        #     settings_menu.settings_menu(running, screen, clock)

        if quit_button.draw(screen):
            print("Quit button clicked!")
            running = False

        pygame.display.flip()
        clock.tick(pygame_config.FPS)
