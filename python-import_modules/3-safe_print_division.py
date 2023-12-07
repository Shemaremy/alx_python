def safe_print_division(a, b):
   try:
      c = a/b   
      
   except ZeroDivisionError:
    print("Inside result: None")
    print("{} / {} = None".format(a,b))

   except Exception as e:
     print("Error: {}".format(e))

   finally:
    print("Inside result: {}".format(c))



#a = 42
#b = 2
#safe_print_division(a,b)

   

 

