#class definition
class Square:
    def __init__(self, _Square__size):
        #constructor definition by using init
        self._Square__size = _Square__size
        #Telling the computer to initialise an instance

    def get_size(self):
        #A method definition to return everything we need
        return self._Square__size

#Instantiation
#my_square = Square(5)

#Accessing the private attribute using a method
#print("Size of the square:", my_square.get_size())


