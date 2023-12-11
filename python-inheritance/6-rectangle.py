'''
The below program will be
telling more about inhertitance
in python programming
'''
class BaseGeometry:
    '''
    The below program will be
    telling more about inhertitance
    in python programming
    '''  

def area(self):
        raise NotImplementedError("area() is not implemented.")

def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")
        if value <= 0:
            raise ValueError(f"{name} must be greater than zero.")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)


try:
    rectangle = Rectangle(5, 10)
    print("Rectangle created successfully.")
except Exception as e:
    print(f"Error: {e}")
