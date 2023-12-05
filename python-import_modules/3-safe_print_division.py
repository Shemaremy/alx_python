class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     if b<0:
      x=a/(-b)
     else:
      x=a/b 
    
     return a/b

try:
    a=10
    b=-2
    pass

except ZeroDivisionError:
    print("Inside result None")

finally:
     if b == 0:
        print("{} / {} = None".format(a,b))
      
     elif b < 0:
        print("Inside result: {}".format(safe_print_division(a,b)))
        
     else:
        print("Inside result: {}".format(safe_print_division(a,b)))
        

        


