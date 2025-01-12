from sympy import Matrix, ZZ
import time

from sage.all import *
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from randMatrixCreate import load_matrices_from_json

size = 3
for size in range(3,26):
    start_time = time.time()

    loaded_matrices = load_matrices_from_json("matrices/"+str(size) + 'x' + str(size)+'_matrices.json')
    # Print loaded matrices
    for idx, matrix in enumerate(loaded_matrices, 1):
        smt = Matrix(matrix)
        A,L,R = smt.smith_form()
        # print(A)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"for {size}x{size} Execution time: {execution_time} seconds")



# for 3x3 Execution time: 0.16206026077270508 seconds
# for 4x4 Execution time: 0.2035984992980957 seconds
# for 5x5 Execution time: 0.37270021438598633 seconds
# for 6x6 Execution time: 0.3284637928009033 seconds
# for 7x7 Execution time: 0.40412092208862305 seconds
# for 8x8 Execution time: 0.6498053073883057 seconds
# for 9x9 Execution time: 0.6672310829162598 seconds
# for 10x10 Execution time: 0.7826416492462158 seconds
# for 11x11 Execution time: 0.8900682926177979 seconds
# for 12x12 Execution time: 0.9985175132751465 seconds
# for 13x13 Execution time: 1.2476534843444824 seconds
# for 14x14 Execution time: 1.3700883388519287 seconds
# for 15x15 Execution time: 1.5488977432250977 seconds
# for 16x16 Execution time: 1.7212347984313965 seconds
# for 17x17 Execution time: 2.395354747772217 seconds
# for 18x18 Execution time: 4.047799825668335 seconds
# for 19x19 Execution time: 1.9518587589263916 seconds
# for 20x20 Execution time: 3.607682943344116 seconds
# for 21x21 Execution time: 4.086221218109131 seconds
# for 22x22 Execution time: 5.659216642379761 seconds
# for 23x23 Execution time: 5.198996305465698 seconds
# for 24x24 Execution time: 5.757007122039795 seconds
# for 25x25 Execution time: 4.9045090675354 seconds