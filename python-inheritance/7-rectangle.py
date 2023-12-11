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
    
class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() is not implemented.")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")
        if value <= 0:
            raise ValueError(f"{name} must be greater than zero.")

        return value

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


try:
    rectangle = Rectangle(5, 10)
    print("Area:", rectangle.area())
    print(str(rectangle))
except Exception as e:
    print(f"Error: {e}")