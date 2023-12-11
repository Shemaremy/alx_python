class Square:
    def __init__(self, size=0):
        # Validate if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")

        # Validate if size is greater than or equal to zero
        if size < 0:
            raise ValueError("size must be greater or equal to zero.")

        # If validations pass, set the size as a private instance attribute
        self.__size = size

    def get_size(self):
        return self.__size

# Example usage:
try:
    # Create a Square instance with size 5
    square_instance = Square(5)
    print("Size of the square:", square_instance.get_size())

    # Attempt to create a Square instance with a non-integer size
    invalid_square = Square("invalid")
except TypeError as e:
    print(f"Error: {e}")

try:
    # Attempt to create a Square instance with a negative size
    negative_square = Square(-3)
except ValueError as e:
    print(f"Error: {e}")