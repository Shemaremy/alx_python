"""
Creating a base class and 
everything will be included inside here
"""
class Base:
    """
    Base class with an id attribute and basic getters and setters.
    """
    def __init__(self, id=None):
        """
        Base class constructor.

        Parameters:
        - id: Optional identifier.
        """
        self.id = id

    def get_id(self):
        """
        Getter for the id attribute.

        Returns:
        - Current id value.
        """
        return self.id

    def set_id(self, new_id):
        """
        Setter for the id attribute.

        Parameters:
        - new_id: New id value.
        """
        self.id = new_id


class Rectangle(Base):
    """
    Rectangle class that inherits from Base with additional attributes
    for width, height, x, and y. It provides getters and setters for each attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle class constructor. Calls the superclass constructor and assigns
        values to width, height, x, and y.

        Parameters:
        - width: Width of the rectangle.
        - height: Height of the rectangle.
        - x: X-coordinate of the rectangle (default is 0).
        - y: Y-coordinate of the rectangle (default is 0).
        - id: Optional identifier.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """
        Getter for the width attribute.

        Returns:
        - Current width value.
        """
        return self.__width

    def set_width(self, new_width):
        """
        Setter for the width attribute.

        Parameters:
        - new_width: New width value.
        """
        self.__width = new_width

    def get_height(self):
        """
        Getter for the height attribute.

        Returns:
        - Current height value.
        """
        return self.__height

    def set_height(self, new_height):
        """
        Setter for the height attribute.

        Parameters:
        - new_height: New height value.
        """
        self.__height = new_height

    def get_x(self):
        """
        Getter for the x attribute.

        Returns:
        - Current x value.
        """
        return self.__x

    def set_x(self, new_x):
        """
        Setter for the x attribute.

        Parameters:
        - new_x: New x value.
        """
        self.__x = new_x

    def get_y(self):
        """
        Getter for the y attribute.

        Returns:
        - Current y value.
        """
        return self.__y

    def set_y(self, new_y):
        """
        Setter for the y attribute.

        Parameters:
        - new_y: New y value.
        """
        self.__y = new_y

