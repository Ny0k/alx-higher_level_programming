#!/usr/bin/python3
"""Module containing the `Rectangle` class inheriting from
`BaseGeometry` class.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Raises:
        TypeError: If width or height is not a positive integer.

    Note:
        The Rectangle class inherits from BaseGeometry and enforces
        positive integer validation for both width and height.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        # Validate width and height as positive integers
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Set width and height as private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """Implement area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
