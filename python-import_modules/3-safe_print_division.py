a = 10
b = 2

def safe_print_division(a, b):
     if b<0:
      x="Inside reslt: {}".format(a/b)
      c=a/b
     elif b>0:
       
      x="Inside lt: {}".format(a/b)
      c=a/b
      return c 

try:
    a = 10
    b = 2

except ZeroDivisionError:
    print("Inside result None")

finally:
   print("Inside result: {}".format(safe_print_division(a,b)))

 

