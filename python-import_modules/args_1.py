def numberofargs (args):
    n = len(args)

    if n == 0:
        x=print(len(args), "ments.")
    elif n == 1:
        x=print(len(args),"argument:")
        x=print("{}: {}".format(n,args[0]))
    else:
        x=print(n,"arguments:")
        m=1
        a=0
        for i in args:            
            x=print("{}: {}".format(m,args[a]))
            m=m+1
            a=a+1
            
    return x


            
