"""Define a reusable button component for the Pygame client."""
from dataclasses import dataclass

import pygame

from settings import pygame_config
from utils import validate_color


@dataclass
class Button:
    """
    A class representing a button component in the Pygame client.
    """
    coords: tuple
    width: int
    height: int

    text: str
    text_color: tuple

    color: tuple
    hover_color: tuple
    shadow_color: tuple

    elevation: int

    def __post_init__(self):
        """
        Check if the data is valid. 
        Initialize the button's rectangle and text surface.
        """
        if len(self.coords) != 2:
            raise ValueError("Coordinates must be a tuple (x, y).")

        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers.")

        for color in [self.color, self.hover_color, self.shadow_color, self.text_color]:
            if not validate_color(color):
                raise ValueError(
                    f"Invalid color: {color}. Must be a tuple of three integers between 0 and 255."
                )

        self._dynamic_elevation = self.elevation
        self._pressed = False
        self._current_color = self.color

        self._rect = pygame.Rect(self.coords[0], self.coords[1], self.width, self.height)
        self._text_surface = pygame_config.MAIN_FONT.render(self.text, True, self.text_color)
        self._text_rect = self._text_surface.get_rect(center=self._rect.center)
        self._shadow_rect = pygame.Rect(self.coords[0], self.coords[1], self.width, self.elevation)

    def draw(self, surface: pygame.Surface) -> bool:
        """
        Draw the button on the given surface.
        """
        self._rect.y = self.coords[1] - self._dynamic_elevation
        self._text_rect.center = self._rect.center

        self._shadow_rect.midtop = self._rect.midtop
        self._shadow_rect.height = self._rect.height + self._dynamic_elevation

        pygame.draw.rect(surface, self.shadow_color, self._shadow_rect, border_radius=12)
        pygame.draw.rect(surface, self.color, self._rect, border_radius=12)
        surface.blit(self._text_surface, self._text_rect)
        return self._check_click()

    def _check_click(self) -> bool:
        """
        Check if the button is clicked based on the mouse position.
        """
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self._rect.collidepoint(mouse_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self._pressed = True
                self._dynamic_elevation = 0
            else:
                self._dynamic_elevation = self.elevation
                if self._pressed:
                    self._pressed = False
                    action = True
        else:
            self._dynamic_elevation = self.elevation
            self.color = self._current_color

        return action


class ButtonBuilder:
    """
    A builder class for constructing Button instances step-by-step.
    """

    def __init__(self):
        """
        Initialize the builder with default button configuration values.
        """
        self._coords = (0, 0)
        self._width = 100
        self._height = 50
        self._text = "Button"
        self._text_color = (255, 255, 255)
        self._color = (0, 0, 255)
        self._hover_color = (0, 100, 255)
        self._shadow_color = (50, 50, 50)
        self._elevation = 5

    def set_coords(self, coords: tuple):
        """
        Set the (x, y) coordinates of the button.
        """
        if len(coords) != 2:
            raise ValueError("Coordinates must be a tuple (x, y).")

        self._coords = coords
        return self

    def set_width(self, width: int):
        """
        Set the width of the button in pixels.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")

        self._width = width
        return self

    def set_height(self, height: int):
        """
        Set the height of the button in pixels.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")

        self._height = height
        return self

    def set_text(self, text: str):
        """
        Set the text label displayed on the button.
        """
        self._text = text
        return self

    def set_text_color(self, text_color: tuple):
        """
        Set the RGB color tuple for the button's text.
        """
        if not validate_color(text_color):
            raise ValueError(
                f"""Invalid text color: {text_color}.
                Must be a tuple of three integers between 0 and 255."""
            )

        self._text_color = text_color
        return self

    def set_color(self, color: tuple):
        """
        Set the default RGB background color of the button.
        """
        if not validate_color(color):
            raise ValueError(
                f"""Invalid color: {color}.
                Must be a tuple of three integers between 0 and 255."""
            )

        self._color = color
        return self

    def set_hover_color(self, hover_color: tuple):
        """
        Set the RGB background color of the button when hovered.
        """
        if not validate_color(hover_color):
            raise ValueError(
                f"""Invalid hover color: {hover_color}.
                Must be a tuple of three integers between 0 and 255."""
            )

        self._hover_color = hover_color
        return self

    def set_shadow_color(self, shadow_color: tuple):
        """
        Set the RGB color of the button's bottom shadow.
        """
        if not validate_color(shadow_color):
            raise ValueError(
                f"""Invalid shadow color: {shadow_color}.
                Must be a tuple of three integers between 0 and 255."""
            )

        self._shadow_color = shadow_color
        return self

    def set_elevation(self, elevation: int):
        """
        Set the 3D elevation offset of the button in pixels.
        """
        if elevation < 0:
            raise ValueError("Elevation must be a non-negative integer.")

        self._elevation = elevation
        return self

    def build(self) -> Button:
        """
        Construct and return the configured Button instance.
        """
        return Button(
            coords=self._coords,
            width=self._width,
            height=self._height,
            text=self._text,
            text_color=self._text_color,
            color=self._color,
            hover_color=self._hover_color,
            shadow_color=self._shadow_color,
            elevation=self._elevation
        )
