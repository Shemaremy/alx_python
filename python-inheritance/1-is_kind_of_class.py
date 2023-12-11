'''
The below program will be
telling more about inhertitance
in python programming
'''
def is_kind_of_class(obj, a_class):
    '''
    The below program will be
    telling more about inhertitance
    in python programming
    '''    
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)

# Example usage:
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

obj = ChildClass()

# Check if obj is an instance of ParentClass or inherited from ParentClass
result = is_kind_of_class(obj, ParentClass)

#print(result)  # Output: True