def numberofargs (args):
    n = len(args)

    if n == 0:
        x=print(len(args), "arguments.")
    elif n == 1:
        x=print(len(args),"argument:")
        x=print(len(args),":",args[0])
    else:
        x=print(n,"arguments:")
        m=1
        a=0
        for i in args:
            x=print(m,":",args[a])
            m=m+1
            a=a+1
            
    return x


            
