# 
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
     last = number%10

     if last > 5:
         print("Last digit of" , number , "is" , last, "and is greater than 5" )

     elif last == 0:
         print("Last digit of" , number , "is" , last, "and is 0" )
     
     elif last < 6 and last > 0:
         print("Last digit of" , number , "is" , last, "and is less than 6 not 0" )


elif number < 0:
     last = number % -10
     if last == 0:
         print("Last digit of" , number , "is" , last, "and is 0" )
     elif last > 5:
         print("Last digit of" , number , "is" , last, "and is greater than 5" )
     elif last < 6 and last < 0:
         print("Last digit of" , number , "is" , last, "and is less than 6 not 0" )


