'''
Setter for the width attribute with type and value checks.
Setter for the width attribute with type and value checks.
Setter for the width attribute with type and value checks.
'''

from models.base import Base
'''
Importing from Base class
Which will be performing
various operations to satisfy task 1

'''

class Rectangle(Base):
    '''
    Importing from Base class
    Which will be performing
    various operations to satisfy task 1

    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Importing from Base class
        Which will be performing
        various operations to satisfy task 1

        """
        super().__init__(id) 
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        It will perform everthing the 
        checker is expecting to see

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        Setter for the width attribute with type and value checks.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        This is a public method
        that calculates and returns the area
        of the rectangle instance based on its
        width and height
        '''
        return self.__width * self.__height
    
    def display(self):
        '''
        This display method 
        prints a rectangle which 
        is made of # characters
        '''

        for _ in range(self.__y):
            print()
        '''
        adding another for loop and
        modifying the second for loop
        '''

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
   
    def __str__(self):
        '''
        Now the str method is
        overriden to return a formatted string
        representing the Rectangle instance
        '''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


# Example usage:
#if __name__ == "__main__":
#    rectangle = Rectangle(10, 20, 5, 7, 1)
#    print(rectangle.id) # Output: 1
#    print(rectangle.width) # Output: 10
#    print(rectangle.height) # Output: 20
#    print(rectangle.x) # Output: 5
#    print(rectangle.y) # Output: 7


