def no_c(my_string):
    a=''.join(char for char in my_string  if char.lower() not in {'c'})
    return a



word = "School"
new_word = no_c(word)

 
