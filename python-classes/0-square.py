'''
The below program will be
telling us the size of our square
'''
#class definition

class Square:
    '''
    Here comes a class definition
    which contais objects
    such as the methods you're seeing below
    '''
    def __init__(self, _Square__size):
     #constructor definition by using init
    
        self._Square__size = _Square__size
   
#Initialisation 
    def get_size(self):


#A method to return the sixe of our square

        return self._Square__size

#Instantiation
#my_square = Square(5)

#Accessing the private attribute using a method
#print("Size of the square:", my_square.get_size())


