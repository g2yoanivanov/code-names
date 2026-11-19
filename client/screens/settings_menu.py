"""Settings menu screen for the Pygame client."""
import pygame

from client.components.button import ButtonBuilder
from settings import pygame_config


class SettingsMenuScreen:
    """
    A class representing the settings menu screen.
    """

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock):
        """
        Initialize the settings menu screen and its buttons.
        """
        self.screen = screen
        self.clock = clock
        self.running = True
        self._create_buttons()

    def _create_buttons(self) -> None:
        """
        Create and position the settings menu buttons based on the current screen center.
        """
        center = self.screen.get_rect().center
        btn_x = center[0] - pygame_config.BTN_WIDTH // 2

        self.fullscreen_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1] - pygame_config.BTN_SPACING))
            .set_text("Fullscreen")
            .build()
        )

        self.windowed_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1]))
            .set_text("800x600")
            .build()
        )

        self.back_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1] + pygame_config.BTN_SPACING))
            .set_text("Done")
            .build()
        )

    def run(self) -> bool:
        """
        Run the settings menu loop.
        Returns True when returning to the main menu, or False if the window was closed.
        """
        pygame.display.set_caption("Settings Menu")
        self.running = True

        while self.running:
            self.screen.fill(pygame_config.BG_MAIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False

            if self.fullscreen_button.draw(self.screen):
                self.screen = pygame.display.set_mode(
                    pygame_config.FULLSCREEN_SIZE, pygame.FULLSCREEN
                )
                self._create_buttons()

            if self.windowed_button.draw(self.screen):
                self.screen = pygame.display.set_mode(pygame_config.SCREEN_SIZE)
                self._create_buttons()

            if self.back_button.draw(self.screen):
                self.running = False

            pygame.display.flip()
            self.clock.tick(pygame_config.FPS)

        return True
