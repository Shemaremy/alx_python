#
import random
number = random.randint(-10, 10)
# YOUR CODE HERE

 
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
