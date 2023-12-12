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
    
    return issubclass(type(obj), a_class) if obj > 1 else False



#a = 1
#print(inherits_from(a, int))


#a = True
#result = inherits_from(a,  BaseClass)
#print(result)