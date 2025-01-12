from sympy import Matrix, ZZ
import time

from sage.all import *
import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
from randMatrixCreate import load_matrices_from_json

size = 3
for size in range(3,26):
    start_time = time.time()

    loaded_matrices = load_matrices_from_json("matrices/"+str(size) + 'x' + str(size)+'_matrices.json')
    # Print loaded matrices
    for idx, matrix in enumerate(loaded_matrices, 1):
        smt = Matrix(matrix)
        H, U = matrix_integer_dense_hnf.hnf_with_transformation(smt)
        # print(H)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"for {size}x{size} Execution time: {execution_time} seconds")

# for 3x3 Execution time: 0.7627301216125488 seconds
# for 4x4 Execution time: 2.550016164779663 seconds
# for 5x5 Execution time: 2.6247854232788086 seconds
# for 6x6 Execution time: 1.4240014553070068 seconds
# for 7x7 Execution time: 2.9237425327301025 seconds
# for 8x8 Execution time: 3.0591399669647217 seconds
# for 9x9 Execution time: 3.285869836807251 seconds
# for 10x10 Execution time: 3.4272022247314453 seconds
# for 11x11 Execution time: 3.806929111480713 seconds
# for 12x12 Execution time: 3.8678743839263916 seconds
# for 13x13 Execution time: 4.146852493286133 seconds
# for 14x14 Execution time: 4.389949321746826 seconds
# for 15x15 Execution time: 3.21351957321167 seconds
# for 16x16 Execution time: 4.945457696914673 seconds
# for 17x17 Execution time: 5.537517070770264 seconds
# for 18x18 Execution time: 6.067340850830078 seconds
# for 19x19 Execution time: 6.5953545570373535 seconds
# for 20x20 Execution time: 6.987786054611206 seconds
# for 21x21 Execution time: 6.044969320297241 seconds
# for 22x22 Execution time: 8.055599927902222 seconds
# for 23x23 Execution time: 8.912620544433594 seconds
# for 24x24 Execution time: 7.831480026245117 seconds
# for 25x25 Execution time: 10.004392862319946 seconds
# for 26x26 Execution time: 14.474491119384766 seconds
# for 27x27 Execution time: 19.696032762527466 seconds
# for 28x28 Execution time: 20.38293480873108 seconds
# for 29x29 Execution time: 23.65014123916626 seconds
# for 30x30 Execution time: 23.828503847122192 seconds
# A = Matrix([[12, 6, 4], [3, 9, 6], [2, 16, 14]])

# H, U = matrix_integer_dense_hnf.hnf_with_transformation(A)

# print(H)
# print(U)

# # snf = smith_normal_form(A, domain=ZZ)
# hnf = hermite_normal_form(A)

# # for i in range(snf.rows):
# #     print(snf.row(i))
# print()
# for i in range(hnf.rows):
#     print(hnf.row(i))

