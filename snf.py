import numpy as np



def gcdExtended(a, b):

    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y



def smith_form(matrix):

    A = np.array(matrix, dtype=np.longlong)
    # Dimensions of the matrix
    m, n = A.shape
    i = j = 0

    def rearrange_rows_and_cols(matrix, pivot_i, pivot_j):
        min_value = matrix[pivot_i, pivot_j]

        min_i = pivot_i
        min_j = pivot_j

        row ,col = pivot_i, pivot_j
        while row < m:
            if matrix[row, col] != 0:
                if abs(matrix[row, col]) < (min_value):
                    min_value = abs(matrix[row, col])
                    min_i = row
                    min_j = col
            row += 1
        while col < n:
            if matrix[pivot_i, col] != 0:
                if abs( matrix[pivot_i, col]) < (min_value):
                    min_value = abs(matrix[pivot_i, col])
                    min_i = pivot_i
                    min_j = col
            col += 1
        print("-------------------------------------------")
        print(min_i, min_j)
        print(min_value)
        if min_i != pivot_i:
            print("Swap Rows")
            matrix[[pivot_i, min_i]] = matrix[[min_i, pivot_i]]
        else:
            print("Swap Cols")
            matrix[:,[pivot_j, min_j]] = matrix[:,[min_j, pivot_j]]


    def extend_pivot_row( matrix, pivot_i, pivot_j, dest_i, dest_j):
        print("-------------------------------------------")
        print("Extend Pivot Row")
        gcd , x, y = gcdExtended(matrix[pivot_i,pivot_j], matrix[dest_i,dest_j])
        print(f"Pivot = {matrix[pivot_i,pivot_j]} , Dest = {matrix[dest_i,dest_j]}")
        print(f"R1 = {matrix[pivot_i,:]}\nR2 = {matrix[dest_i,:]}")
        print(f"R1 = R1 * {x} + R2 * {y} = {gcd}")
        print("\nBefore")
        print(matrix)

        matrix[pivot_i,:] = x * matrix[pivot_i,:] + y * matrix[dest_i,:]

        print("\nAfter")
        print(matrix)
        print("-------------------------------------------")

    def extend_pivot_col( matrix, pivot_i, pivot_j, dest_i, dest_j):
        print("-------------------------------------------")
        print("Extend Pivot Col")
        gcd , x, y = gcdExtended(matrix[pivot_i,pivot_j], matrix[dest_i,dest_j])
        print (f"Pivot = {matrix[pivot_i,pivot_j]} , Dest = {matrix[dest_i,dest_j]}")
        print (f"C1 = {matrix[:,pivot_j]}\nC2 = {matrix[:,dest_j]}")
        print (f"C1 = C1 * {x} + C2 * {y} = {gcd}")
        print("\nBefore")
        print (matrix)

        matrix[:,pivot_j] = x * matrix[:,pivot_j] + y * matrix[:,dest_j]

        print("\nAfter")
        print(matrix)
        print("-------------------------------------------")

    def eleminate_row (matrix, pivot_i, pivot_j, dest_i, dest_j):
        print("-------------------------------------------")
        print("Eleminate Row")
        print(f"Pivot Row = {matrix[pivot_i,:]}")
        print(f"Dest Row = {matrix[dest_i,:]}")
        print(f"R2 = R2 - R1 * {matrix[dest_i,dest_j] // matrix[pivot_i,pivot_j]}")
        print("\nBefore")
        print(matrix)

        matrix[dest_i,:] = matrix[dest_i,:] - (matrix[dest_i,dest_j] // matrix[pivot_i,pivot_j]) * matrix[pivot_i,:]

        print("\nAfter")
        print(matrix)
        print("-------------------------------------------")

    def eleminate_col (matrix, pivot_i, pivot_j, dest_i, dest_j):
        print("-------------------------------------------")
        print("Eleminate Col")
        print(f"Pivot Col = {matrix[:,pivot_j]}")
        print(f"Dest Col = {matrix[:,dest_j]}")
        print(f"C2 = C2 - C1 * {matrix[dest_i,dest_j] // matrix[pivot_i,pivot_j]}")
        print("\nBefore")
        print(matrix)

        matrix[:,dest_j] = matrix[:,dest_j] - (matrix[dest_i,dest_j] // matrix[pivot_i,pivot_j]) * matrix[:,pivot_j]

        print("\nAfter")
        print(matrix)
        print("-------------------------------------------")

    clear = False


    while i < m :

        row = i + 1

        clear = True

        if True:
            print('Before')
            print (A)
            rearrange_rows_and_cols(A, i, i)
            print('After')
            print (A)


        while row < m:
            if A [row,i] == 0:
                row += 1
                continue

            clear = False
            extend_pivot_row(A, i, i, row, i)
            eleminate_row(A, i, i, row, i)
            row += 1

        col = i + 1
        while col < n:
            if A[i,col] == 0:
                col += 1
                continue
            clear = False
            extend_pivot_col(A, i, i, i, col)
            eleminate_col(A, i, i, i, col)
            # print(i,'',col)
            col += 1


        if clear:
            if A[i,i] <= 0:
                A[i,:] = -1 * A[i,:]
            i += 1

    pivots = 0

    while pivots < m-1:
        gcd , x, y = gcdExtended(A[pivots,pivots], A[pivots+1,pivots+1])
        A[pivots+1,pivots+1] =  (A[pivots,pivots] // gcd )* A[pivots+1,pivots+1]
        A[pivots,pivots] = gcd
        pivots += 1
    return A


# Example usage
# matrix = [
#     [6, 9, 15],
#     [2, 3, 5],
#     [12, 15, 30]
# ]
# matrix= [
#      [2, 4, 4],
#      [-6, 6, 12],
#      [10, -4, -16]
# ]

# matrix= [
#     [2, 4, 4,6],
#     [-6, 6, 12, 8],
#     [10, -4, -16, 24]
# ]

# matrix= [
#     [-1, 4, 4] ,
#     [2, 0, 12],
#     [10, -4, 0]
# ]

matrix= [
    [7,-2, -4] ,
    [10, 3, 12],
    [3, 4, 7]
]



# matrix =[

#     [27, 80, 12, 19,  5],
#  [57, 22, 40, 49, 61],
#  [63, 74, 76, 68, 34],
#  [34, 33, 83, 45, 51],
# [48, 48, 67,  7, 76]]

# matrix= [

#        [1, -1, 0, 2, -7, -5, 9, -6, 0, 2, -10, -8, -10, -9, 0],
#    [0, -4, 1, -10, -8, -8, 2, 7, -1, -6, 6, -2, 0, 4, 1],
#    [-2, 5, -9, 8, -6, -5, 5, -4, -1, -10, 2, 4, 4, -5, 2],
#    [-8, -2, -3, 3, -8, -8, 9, 8, -4, 0, -9, -4, 0, -4, -1],
#    [-4, 6, -9, 5, 8, -5, 3, -2, -6, 2, 0, -1, -8, 1, -3],
#    [-7, -4, -9, 4, 8, 1, 5, 5, 6, 3, -4, 8, 8, -8, -8],
#    [-5, -4, 1, -10, 6, -5, -4, 0, 4, -9, -7, -8, -2, 5, 3],
#    [-6, 9, 0, -5, 4, -3, -10, 5, 6, -9, -8, 9, 2, -4, -9],
#    [6, -8, 6, 7, -2, 3, -7, -3, 7, 2, -7, -3, -8, -3, 8],
#    [2, -6, -7, -3, 8, 9, 3, 4, 2, 4, -1, 7, -3, -7, 5],
#    [-7, 1, 7, -4, -10, -6, -2, -6, 2, -1, -8, 3, 3, 9, 7],
#    [-1, 6, 2, 9, 1, 7, -4, -7, -3, -1, 5, 4, 4, 1, -6],
#    [-4, -10, 7, -5, 3, 1, 0, 3, -5, 7, 5, -10, -8, 9, 7],
#    [-2, 7, 6, 0, -8, 3, -10, 4, 5, 7, 0, 5, 5, -7, 0],
#    [2, 7, 2, 0, 5, -7, 2, 0, -4, 1, 4, 3, 0, 8, -8]

# ]

matrix2 = [


]

m = np.array(matrix, dtype=int)
A = smith_form(m)
# A = A/ 12
# print(m)
print(A)
# for i in range(0, len(A)):
#     print(A[i])
# print(m[:,0])
# m[:,0] = m[:,0]*2
#
# [  1    0     0                0                0                0                0                0                0                0                0                0                0                0                0]
# [  0    1     0                0                0                0                0                0                0                0                0                0                0                0                0]
# [  0    0     1                0                0                0                0                0                0                0                0                0                0                0                0]
# [  0    0     0                1                0                0                0                0                0                0                0                0                0                0                0]
# [  0    0     0                0                1                0                0                0                0                0                0                0                0                0                0]
# [  0    0     0                0                0                1                0                0                0                0                0                0                0                0                0]
# [  0    0     0                0                0                0                1                0                0                0                0                0                0                0                0]
# [  0    0     0                0                0                0                0                1                0                0                0                0                0                0                0]
# [  0    0     0                0                0                0                0                0                1                0                0                0                0                0                0]
# [  0    0     0                0                0                0                0                0                0                1                0                0                0                0                0]
# [  0    0     0                0                0                0                0                0                0                0                1                0                0                0                0]
# [  0    0     0                0                0                0                0                0                0                0                0                1                0                0                0]
# [  0    0     0                0                0                0                0                0                0                0                0                0                1                0                0]
# [  0    0     0                0                0                0                0                0                0                0                0                0                0                1                0]
# [  0    0     0                0                0                0                0                0                0                0                0                0                0                0 4305041425188585]
