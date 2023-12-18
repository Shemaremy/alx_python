# rectangle.py
'''
Importing from Base class
'''
from base import Base
'''
Creating another class 
called rectangle
'''
class Rectangle(Base):
    """
    A class representing a Rectangle object, inheriting from the Base class.

    Attributes:
    - __width (int): A private instance attribute representing the width of the rectangle.
    - __height (int): A private instance attribute representing the height of the rectangle.
    - __x (int): A private instance attribute representing the x-coordinate of the rectangle.
    - __y (int): A private instance attribute representing the y-coordinate of the rectangle.

    Methods:
    - __init__: The constructor method to initialize the Rectangle object.
    - width: Getter and setter for the width attribute.
    - height: Getter and setter for the height attribute.
    - x: Getter and setter for the x attribute.
    - y: Getter and setter for the y attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle.
        - y (int): The y-coordinate of the rectangle.
        - id (int): An optional parameter representing the identifier for the object.
        """
        super().__init__(id) # Call the superclass constructor with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.__y = value

# Example usage:
#if __name__ == "__main__":
#    rectangle = Rectangle(10, 20, 5, 7, 1)
#    print(rectangle.id) # Output: 1
#    print(rectangle.width) # Output: 10
#    print(rectangle.height) # Output: 20
#    print(rectangle.x) # Output: 5
#    print(rectangle.y) # Output: 7


