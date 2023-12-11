'''
The below program will be
telling us the size of our square
'''
class Square:
    '''
    Here comes a class definition
    which contais objects
    such as the methods you're seeing below
    '''

    def __init__(self, size=0):
        # Validate if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Validate if size is greater than or equal to zero
        if size < 0:
            raise ValueError("size must be >= 0")

        # If validations pass, set the size as a private instance attribute
        self.__size = size

    def get_size(self):
        return self.__size

# Example usage:
try:
    # Create a Square instance with size 5
    square_instance = Square(5)
    

    # Attempt to create a Square instance with a non-integer size
    invalid_square = Square("invalid")
except TypeError as e:
    pass

try:
    # Attempt to create a Square instance with a negative size
    negative_square = Square(-3)
except ValueError as e:
    pass