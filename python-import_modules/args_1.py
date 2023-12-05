def numberofargs ():
    args=[] 
    
    if len(args) == 0:
        x=(len(args), "arguments.")
    elif len(args) == 1:
        x=(len(args),"argument:")
        x=("{}: {}".format(len(args),args[0]))
    else:
        x=(len(args),"arguments:")
        m=1
        a=0
        for i in args:            
            x=("{}: {}".format(m,args[a]))
            m=m+1
            a=a+1
            
    return x


            
