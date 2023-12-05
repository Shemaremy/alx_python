class Flacko(Exception):
 """Custom exception for negative values."""

def safe_print_division(a, b):
     if b<0:
      x=a/(-b)
     else:
      x=a/b 
    
     return x

try:
    a=10
    b=2
    #print(a if a>b else b)

except ZeroDivisionError:
    print("Inside result None")

finally:
     if b == 0:
        print("{} / {} = None".format(a,b))
      
     elif b < 0:
        print("Inside result: {}".format(safe_print_division(10,-2)))
        
     else:
        print("Inside result: {}".format(safe_print_division(10,2)))
        

        


