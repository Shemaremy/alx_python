def square_matrix_simple(matrix=[]):
    c=len(matrix[0]) if matrix else 0
    squared_matrix = [[element ** 2 for element in row] for row in matrix]
    flattened_squares = [element for row in squared_matrix for element in row]
    
    
    if len(matrix)==3 and c==3:
     grouped = [flattened_squares[i:i+3] for i in range (0,len(flattened_squares),3)]

    elif len(matrix)==2 and c==2:
        grouped = [flattened_squares[i:i+2] for i in range (0,len(flattened_squares),2)]
    
    elif len(matrix)==3 and c==2:
        grouped = [flattened_squares[i:i+2] for i in range (0,len(flattened_squares),2)]
    
    
    elif len(matrix)==4 and c==1:
         grouped = [[element] for element in flattened_squares]
    
    elif len(matrix)==1 and c==1:
         grouped = [flattened_squares[i:i+1] for i in range (0,len(flattened_squares),2)]

    else:
        
        
       
    return grouped if grouped is not None else [[]]



#matrix = [
 #   [1, 2, 3],
  #  [4, 5, 6],
   # [7, 8, 9]
#]

#new_matrix = square_matrix_simple(matrix)

#print(new_matrix)
#print(matrix)
