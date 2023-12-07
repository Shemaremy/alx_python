def safe_print_division(a, b):
   try:
      result = a/b   
      
   except ZeroDivisionError:
    print("Inside result: None")
    #print("{:d} / {:d} = None".format(a,b))
    return None

   except Exception as e:
     print("Error: {}".format(e))
     return None

   else:
      return result 

   finally:
    if 'result' not in locals():
     return("None")
    else:
       print("Inside result: {}".format(a/b))


#a = 0
#b = 10
#result = safe_print_division(a, b)
#print("{:d} / {:d} = {}".format(a, b, result))
