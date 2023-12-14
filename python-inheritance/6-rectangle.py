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
    if not isinstance (value, int) or value <= 0:
        raise ValueError("width must be greater than 0")



#try:
#    r = Rectangle(0, 4)
#except Exception as e:
#    print("[{}] {}".format(e.__class__.__name__, e))

#print(issubclass(Rectangle, BaseGeometry))
