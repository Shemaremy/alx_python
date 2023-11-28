
def fibonacci_sequence(n):
     a=0
     b=1
     print("[" , end="")
     for i in range(0,n):
         if i<=1:
             print(i , end=", ")
         
    
         elif i>1 and i<n-1:
             c = a+b
             print(c , end=", ")
             a = b
             b = c
         
         else:
             c=a+b   
             print(c,end="]")
            
 
     