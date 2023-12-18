'''
Importing from Base class
'''
from models.base import Base
'''
Creating another class 
called rectangle
'''
class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializinf a Rectangle object
        """
        super().__init__(id) 
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


