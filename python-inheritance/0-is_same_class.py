def is_same_class(obj, a_class):
    return isinstance(obj, a_class)

class Remi:
    pass

#mi = Remi()
#r= is_same_class(mi,Remi)
a = 1
print(is_same_class(a, int))
