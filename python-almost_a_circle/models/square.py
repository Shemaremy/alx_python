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

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"