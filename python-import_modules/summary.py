# Understanding of          if __name__ == '__main__':
'''
Apparently, the codeline above will check if the script is run as a main program, or
if the script is  is being imported as a module into another script.

When the code is run as the main one. Immediately, it is assigned as '__main__'
(      if __name__ == '__main__':     ) means if true, it is run as main one. Otherwise, it is imported

Let's take an example. Let the first file be called one.py and another called two.py.
two.py will check if its script is imported as a module or is being run as a main program.


'''




#   one.py file             (Output: Sum is 3)



def add_numbers(a, b):
     return a + b

if __name__ == '__main__':                  
    
    num1 = 1
    num2 = 2
    s = add_numbers(num1, num2)

    print("Sum is" , s)









#     two.py file               (Output:  This script is being imported sir )

from one.py import add_numbers

if __name__ == '__main__':
    
    num1 = 2
    num2 = 3
    m = add_numbers(num1, num2)

    print("Sum is" , s)

else:
    print("This script is being imported sir")

