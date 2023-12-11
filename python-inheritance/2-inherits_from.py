'''
The below program will be
telling more about inhertitance
in python programming
'''
class BaseClass:
    pass
class DerivedClass(BaseClass):
    pass

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
    
    return isinstance(obj, type) and issubclass(type(obj), a_class)


#a = True
#result = inherits_from(a,  BaseClass)
#print(result)