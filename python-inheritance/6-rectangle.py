class BaseGeometry:
    '''
    This is the Class docstring
    (Tring to figure out something. lol)
    '''
    pass

'''
The below program will be
telling more about inhertitance
in python programming
'''
class Rectangle(BaseGeometry):
 '''
 The below program will be
 telling more about inhertitance
 in python programming
 '''
 def __init__(self, width, height):
    '''
    initialises an instance of the class rectangle
    Okay
    '''
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height

 def integer_validator(self, name, value):
    if not isinstance (value, int):
        raise TypeError(f"{name} must be an integer")




#print(issubclass(Rectangle, BaseGeometry))
