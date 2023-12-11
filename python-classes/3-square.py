
'''
The below program will be
telling us the size of our square
'''
class Square:
    #here comes a documented class too
    '''
    Here comes in a class definition
    which contais objects
    such as the methods you're seeing below
    '''    
    def __init__(self, size=0):
        self.size = size  # Using the property setter to validate and set the size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # Validate if size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer.")

        # Validate if size is greater than or equal to zero
        if value < 0:
            raise ValueError("size must be greater or equal to zero.")

        # If validations pass, set the size as a private instance attribute
        self.__size = value

    def area(self):
        # Return the area of the square
        return self.__size ** 2


try:
    # Create a Square instance with size 5 using property setter
    square_instance = Square()
    square_instance.size = 5

    # Access the size using the property getter
    #print("Size of the square:", square_instance.size)

    # Calculate and print the area
    #print("Area of the square:", square_instance.area())

    # Attempt to set size to a non-integer value
    square_instance.size = "invalid"
except TypeError as e:
    #print(f"Error: {e}")
    pass

try:
    # Attempt to set size to a negative value
    square_instance.size = -3
except ValueError as e:
    #print(f"Error: {e}")
    pass