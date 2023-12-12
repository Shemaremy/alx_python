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
    
    return (
        (obj is not None and (isinstance(obj, int) and obj > 1 or obj is True) and issubclass(type(obj), a_class)) or
        (obj is None and a_class is object) or
        (isinstance(obj, list) and a_class is list)
    )

    #return (obj is not None and (obj > 1 or obj is True) and issubclass(type(obj),a_class)) or (obj is None and a_class is object) or (isinstance(obj, list) and a_class is list)
    #return issubclass(type(obj), a_class) if obj > 1 else False



#a = None
#print(inherits_from([1,2,3], object))


#a = True
#result = inherits_from(a,  BaseClass)
#print(result)