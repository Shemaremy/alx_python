
def is_same_class(obj, a_class):

  class Remi:
     pass

  return isinstance(obj, a_class)

a = 1
if is_same_class(a, int):
    pass
    #print(is_same_class(a, int))
    

 

 
