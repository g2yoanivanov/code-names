"""Validation helpers for project data."""

def validate_color(color: tuple) -> bool:
        """
        Validate that the color is a tuple of three integers between 0 and 255.
        """
        if not isinstance(color, tuple) or len(color) != 3:
            return False
        return all(isinstance(c, int) and 0 <= c <= 255 for c in color)