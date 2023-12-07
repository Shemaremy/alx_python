def print_arguments():
    argv = ["Hello", "Holberton" ]
    c = len(argv) 
    
    if c == 0:
        print(len(args), "arguments.")

    else:
        print(f"{c} argument{'' if c == 1 else 's'}:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}") 



            
