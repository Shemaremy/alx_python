def print_arguments(args_list):
    c = len(args_list) 
    
    if c == 0:
        print(len(args), "arguments.")

    else:
        print(f"{c} argument{'' if c == 1 else 's'}:")

        for i, arg in enumerate(args_list, start=1):
            print(f"{i}: {repr(arg)}") 



            
