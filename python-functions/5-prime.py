def is_prime(number):
    if number%2 != 0 and number%3 != 0:
        print("True")

    else:
        print("False")


n=int(input("enter any number : ")) 
is_prime(n)           
