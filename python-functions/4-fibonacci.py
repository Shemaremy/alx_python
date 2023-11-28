
def fibonacci_sequence(n):
    a=0
    b=1
    for i in range(0,n,1):
        if i<=1 :
            m = i
            print(m,end=", ")
        else:
            c=a+b
            m=c
            print(".".join ("{:01d}".format(m),end=","))
            # ",".join()
            a=b
            b=c

    return m
        
      
fibonacci_sequence(6)


         
         
     