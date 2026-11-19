"""Main menu screen for the Pygame client."""
import pygame

from client.components.button import ButtonBuilder
from client.screens.settings_menu import SettingsMenuScreen
from settings import pygame_config


class MainMenuScreen:
    """
    A class representing the main menu screen.
    """

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock):
        """
        Initialize the main menu screen and its buttons.
        """
        self.screen = screen
        self.clock = clock
        self.running = True
        self._create_buttons()

    def _create_buttons(self) -> None:
        """
        Create and position the main menu buttons based on the current screen center.
        """
        center = self.screen.get_rect().center
        btn_x = center[0] - pygame_config.BTN_WIDTH // 2

        self.host_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1] - 2 * pygame_config.BTN_SPACING))
            .set_text("Host Game")
            .build()
        )

        self.join_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1] - pygame_config.BTN_SPACING))
            .set_text("Join Game")
            .build()
        )

        self.settings_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1]))
            .set_text("Settings")
            .build()
        )

        self.quit_button = (
            ButtonBuilder()
            .set_coords((btn_x, center[1] + pygame_config.BTN_SPACING))
            .set_text("Quit")
            .build()
        )

    def run(self) -> None:
        """
        Run the main menu event and rendering loop.
        """
        pygame.display.set_caption("Main Menu")
        self.running = True

        while self.running:
            self.screen.fill(pygame_config.BG_MAIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.host_button.draw(self.screen):
                pass

            if self.join_button.draw(self.screen):
                pass

            if self.settings_button.draw(self.screen):
                settings_screen = SettingsMenuScreen(self.screen, self.clock)
                keep_running = settings_screen.run()
                self.screen = settings_screen.screen
                self._create_buttons()
                pygame.display.set_caption("Main Menu")
                if not keep_running:
                    self.running = False

            if self.quit_button.draw(self.screen):
                self.running = False

            pygame.display.flip()
            self.clock.tick(pygame_config.FPS)
