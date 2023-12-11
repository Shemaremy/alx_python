class Square:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

#Instantiation
my_square = Square(5)

#Accessing the private attribute using a method
print("Size of the square:", my_square.get_size())
