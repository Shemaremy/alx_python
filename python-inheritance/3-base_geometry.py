'''
The below program will be
telling more about inhertitance
in python programming
'''
class BaseGeometry:
   class meta_class:
    pass
    #def __init_subclass__(cls,**kwargs):
     #   pass
    def __dir__(self):
        return [attr for attr in dir(type(self)) if not (attr.startswith("__") and attr.endswith("__")) or attr == "__dir__"]



bg = BaseGeometry()

print(dir(bg))




