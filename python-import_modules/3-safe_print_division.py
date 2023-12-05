

class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     if b<0:
      a=10
      b=-2
      x="Inside reslt: {}".format(a/b)
      c=a/b
     elif b>0:
      a=10
      b=2
      x="Inside lt: {}".format(a/b)
      c=a/b
    
     return a/b 

try:
    pass

    
    
    #print(a if a>b else b)

except ZeroDivisionError:
    print("Inside result None")

finally:
   u = safe_print_division(12,5)
   if u is not None:
    print("Inside result:",u)






   



     
        

        


