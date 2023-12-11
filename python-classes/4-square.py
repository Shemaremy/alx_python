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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("Size must be >= 0.")
        else:
            self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)

 
square_instance = Square(3)
#print(square_instance.area())  # Output: 9
#square_instance.my_print()