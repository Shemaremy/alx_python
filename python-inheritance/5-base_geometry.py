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
        raise Exception("area() is not implemented.")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


bg = BaseGeometry()

try:
    bg.area()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
