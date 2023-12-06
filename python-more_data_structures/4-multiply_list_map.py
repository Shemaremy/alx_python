def multiply_list_map(my_list=[], number=0):
    number = number+1
     
    return  list(map(lambda x: x * number, my_list)) 


#my_list = [1, 2, 3, 4, 5]
#number = 2
#new_list = multiply_list_map(my_list, number)
#print(new_list)
#print(my_list)