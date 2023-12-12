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
class meta_class:

    def dir(cls):
        return [attribute for  attribute in super().dir() if attribute != "init_subclass"] 
