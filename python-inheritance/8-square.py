'''
The below program will be
telling more about inhertitance
in python programming

'''
class Rectangle:
    '''
    The below program will be
    telling more about  inhertitance
    in python programming
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    '''
    The below program will be
    telling more about inhertitance
    in python programming
    '''
    def __init__(self, size):
        self.__integer_validator(size)
        super().__init__(size, size)

    @staticmethod
    def __integer_validator(value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("size must be an integer")

#print(issubclass(Square, Rectangle))
# Example usage:
#try:
#    square = Square(5)
#    print(f"Square area: {square.area()}")
#except ValueError as e:
#    print(f"Error: {e}")