def no_c(my_string):
    a=''.join(char for char in my_string  if char.lower() not in {'c'})
    return a


print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))