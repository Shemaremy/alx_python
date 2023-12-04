def numberofargs (args):
     

    if len(args) == 0:
        x=print(len(args), "arguments.")
    elif len(args) == 1:
        x=print(len(args),"argument:")
        x=print("{}: {}".format(len(args),args[0]))
    else:
        x=print(len(args),"arguments:")
        
        
        for i in args:            
            x=print("{}: {}".format(i,args[i-1]))
            m=m+1
            a=a+1
            
    return x


            
