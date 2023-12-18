'''
Importing from Base class
Which will be performing
various operations to satisfy task 1

'''
from models.rectangle import Rectangle
'''
Importing from Base class
Which will be performing
various operations to satisfy task 1

'''
class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square shape.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object with specified size, x, y, and id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

if __name__ == "__main__":
    # Example usage:
    square = Square(5)
    print(square) # Output: [Square] (None) 0/0 - 5

    square.size = 8
    print(square) # Output: [Square] (None) 0/0 - 8    

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"