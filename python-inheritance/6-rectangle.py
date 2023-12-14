
class BaseGeometry:
    '''
    This is the Class docstring
    (Trying to figure out something. lol)
    '''
    pass

'''
The below program will be
telling more about inheritance
in Python programming
'''
class Rectangle(BaseGeometry):
    '''
    The below program will be
    telling more about inheritance
    in Python programming
    '''
    def __init__(self, width, height):
        '''
        Initializes an instance of the class rectangle
        Okay
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        if not isinstance(value, int) or value <= 0:
            if name == "height":
                raise TypeError("height must be an integer")
            elif name == "width":
                raise TypeError("width must be greater than 0")

#try:
#    r = Rectangle(3, "3")
#except TypeError as e:
#    print("[{}] {}".format(e.__class__.__name__, e))

#try:
#    r = Rectangle(0, 4)
#except TypeError as e:
#    print("[{}] {}".format(e.__class__.__name__, e))
