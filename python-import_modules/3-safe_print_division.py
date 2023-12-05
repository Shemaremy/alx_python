class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     #c=a/b
    
     return a/b

try:
    
    
    

except ZeroDivisionError:
    print("Inside result None")

finally:
     if b == 0:
        print("{} / {} = None".format(a,b))
      
     elif b < 0:
        print("Inside result: {}".format(a,b))
        
     else:
        print("Inside result:", a/b)
        

        


