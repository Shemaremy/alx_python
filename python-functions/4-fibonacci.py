
def fibonacci_sequence(n):
     a=0
     b=1
     
     for i in range(0,n):
         if i==0 or i==1:
             print("[" , i , end=", ")
         else:
             c = a+b
             print(c , end=", ]")
             a = b
             b = c
 
      

       
          
        
     