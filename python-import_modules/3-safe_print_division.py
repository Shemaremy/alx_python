

class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     if b<0:
      x="Inside reslt: {}".format(a/b)
      p=a/b
     elif b>0:
      x="Inside lt: {}".format(a/b)
      p=a/b
    
     return p 

try:
    pass

    
    
    #print(a if a>b else b)

except ZeroDivisionError:
    print("Inside result None")

finally:
   u = safe_print_division(10,2)
   if u is not None:
    print("Inside result:",u)






   



     
        

        


