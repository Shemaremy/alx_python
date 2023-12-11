'''
The below program will be
telling more about inhertitance
in python programming
'''
def inherits_from(obj, a_class):
    '''
    The below program will be
    telling more about inhertitance
    in python programming
    '''     
    return isinstance(obj, type) and issubclass(obj, a_class)

class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

obj = ChildClass()
result = inherits_from(obj, ParentClass)
#print(result)