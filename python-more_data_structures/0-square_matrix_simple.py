def square_matrix_simple(matrix=[]):
    squared_matrix = [[element ** 2 for element in row] for row in matrix]
    flattened_squares = [element for row in squared_matrix for element in row]
    grouped = [flattened_squares[i:i+3] for i in range (0,len(flattened_squares),3)]
    return grouped






 
