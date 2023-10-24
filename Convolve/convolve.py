def convolve(input_matrix):
    '''
    Takes an matrix and returns sums of 3x3 grid
    '''
    
    # Find limits for the main and sub arrays (x and y)
    array_length = len(input_matrix)
    sub_array_length = len(input_matrix[0])

    # New array to hold convolved values
    convolved_array = []

    # Since checks 3 x 3, won't from last two values (same for sub-array)
    for i in range(array_length-2):

        # Sub-arrays which will get added to main array
        temp_array = []

        for j in range(sub_array_length-2):
            temp_array.append(sum_of_3x3_grid(input_matrix, i , j))

        convolved_array.append(temp_array)

    return convolved_array


def sum_of_3x3_grid(matrix, i, j): 
    '''
    Finds the sum from 3x3 grid
    '''
    sum = 0
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            sum += matrix[x][y]
    return sum




#Test Cases
# ===========================================
matrix_1 = [[1, 1, 1, 1, 0], 
            [1, 1, 0, 0, 0], 
            [0, 0, 1, 0, 1], 
            [0.5, 0, 0, 1, 0]]
# oputput >>> [[6, 5, 4], [3.5, 3, 3]]

matrix_2 = [[1, 1, 1], 
            [1, 1, 1], 
            [1, 1, 1], 
            [1, 1, 0]]
# oputput >>> [[9],[8]]

matrix_3 = [[1, 1, 1, 1], 
            [1, 1, 1, 1], 
            [1, 1, 1, 1], 
            [1, 1, 1, 1]]
# oputput >>> [[9, 9], [9, 9]]

def print_output(convolved_array):
    for i in convolved_array:
        print(i)
    print("")

print_output(convolve(matrix_1))
print_output(convolve(matrix_2))
print_output(convolve(matrix_3))
