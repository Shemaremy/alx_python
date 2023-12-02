def numberofargs (args):
    n = len(args)

    if n == 0:
        x=print("0 arguments.")
    elif n == 1:
        x=print("1 argument:")
        x=print("1:",args[0])
    else:
        x=print(n,"arguments:")
        m=1
        a=0
        for i in args:
            x=print(m,":",args[a])
            m=m+1
            a=a+1
    return x
    

 

            
