class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     c=a/b
    
     return c

try:
    a = 10
    b = 2
    c = a/b

    d=10
    e=-2
    f=d/e
     
except ZeroDivisionError:
    print("Inside result None")

finally:
     if b == 0:
        print("{} / {} = None".format(a,b))

     elif e < 0:
        print("Inside result:",f)   
     else:
        print("Inside result:",c)
        

        


