class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     c=a/b
    
     return c

try:
    a = 12
    b = 0
    c = a/b
     
except ZeroDivisionError:
    print("Inside result None")

finally:
     if b == 0:
        print("{} / {} = None".format(a,b))
     else:
        print("Inside result: ",c)
        print("{} / {} = {}".format(a,b,c))

        


