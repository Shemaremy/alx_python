class Square:
    def __init__(self, _Square__size):
        self._Square__size = _Square__size

    def get_size(self):
        return self._Square__size

#Instantiation
#my_square = Square(5)

#Accessing the private attribute using a method
#print("Size of the square:", my_square.get_size())

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
