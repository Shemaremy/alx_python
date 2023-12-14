'''
The below program will be
telling more about inhertitance
in python programming
'''
class BaseGeometry:
   class meta_class:
    

    def __dir__(self):
        return [attr for attr in dir(type(self)) if not (attr.startswith("__") and attr.endswith("__")) or attr == "__dir__"]



bg = BaseGeometry()

print(dir(bg))




