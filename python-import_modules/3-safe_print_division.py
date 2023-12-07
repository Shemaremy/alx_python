def safe_print_division(a, b):
   try:
      result = a/b   
      
   except ZeroDivisionError:
    print("Inside result: None")
    print("{} / {} = None".format(a,b))
    return None

   except Exception as e:
     print("Error: {}".format(e))
     return None

   else:
      return result 

   finally:
    print("Inside result: {}".format(a/b))


 


#a = 42
#b = 2
#safe_print_division(a,b)

   

 

