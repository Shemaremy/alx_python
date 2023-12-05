

class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     if b<0:
      x=a/b
     elif b>0:
      x=a/b
     
    
     return x

try:
    pass

    
    
    #print(a if a>b else b)

except ZeroDivisionError:
    print("Inside result None")

finally:
   u = safe_print_division(10,2)
   if u is not None:
    print("{}".format(u))






   



     
        

        


