def numberofargs (args):
     

    if len(args) == 0:
        x=print(len(args), "arguments.")
    elif len(args) == 1:
        x=print(len(args),"argument:")
        x=print("{}: {}".format(len(args),args[0]))
    else:
        x=print(len(args),"arguments:")
        m=1
        a=0
        for i in args:            
            x=print("{}: {}".format(m,args[a]))
            m=m+1
            a=a+1
            
    return x


            
