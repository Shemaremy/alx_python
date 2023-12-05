def print_matrix_integer(matrix=[[]]):
  c=len(matrix[0]) if matrix else 0
    
  for row in matrix:
        if len(matrix)==1 and c==1:
           print("{:d}".format(*row))

        elif len(matrix)==2 and c==2:
           print("{:d} {:d}".format(*row))

        elif len(matrix)==3 and c==2:
           print("{:d} {:d}".format(*row))   
        
        elif len(matrix)==3 and c==3:
           print("{:d} {:d} {:d}".format(*row))

        elif len(matrix)==4 and c==1:
           print("{:d}".format(*row))   
        
        else:
            print("")

 
#matrix = [[1]]

#print_matrix_integer(matrix)

