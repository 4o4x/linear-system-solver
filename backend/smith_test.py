from smith import smith_normal_form
import time
from randMatrixCreate import load_matrices_from_json
from sympy import Matrix


size = 3
for size in range(3,26):
    start_time = time.time()

    loaded_matrices = load_matrices_from_json("matrices/"+str(size) + 'x' + str(size)+'_matrices.json')
    # Print loaded matrices
    for idx, matrix in enumerate(loaded_matrices, 1):
        smt = Matrix(matrix)
        L,A,R = smith_normal_form(smt)
        # print(H)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"for {size}x{size} Execution time: {execution_time} seconds")

# for 3x3 Execution time: 2.076425313949585 seconds
# for 4x4 Execution time: 4.090488910675049 seconds
# for 5x5 Execution time: 6.8282225131988525 seconds
# for 6x6 Execution time: 11.218446493148804 seconds
# for 7x7 Execution time: 15.812009572982788 seconds
# for 8x8 Execution time: 21.31871271133423 seconds
# for 9x9 Execution time: 28.421658277511597 seconds
# for 10x10 Execution time: 36.64220929145813 seconds
# for 11x11 Execution time: 45.8686728477478 seconds
# for 12x12 Execution time: 59.294870138168335 seconds
# for 13x13 Execution time: 72.20354866981506 seconds
# for 14x14 Execution time: 85.19957089424133 seconds
# for 15x15 Execution time: 102.46785140037537 seconds
# for 16x16 Execution time: 119.906405210495 seconds
# for 17x17 Execution time: 146.5459864139557 seconds
# for 18x18 Execution time: 173.90113711357117 seconds
# for 19x19 Execution time: 205.01177501678467 seconds
# for 20x20 Execution time: 283.0698275566101 seconds
# for 21x21 Execution time: 413.833886384964 seconds
# for 22x22 Execution time: 477.24289751052856 seconds
# for 23x23 Execution time: 1056.939037322998 seconds
# for 24x24 Execution time: 4047.8909747600555 seconds
# for 25x25 Execution time: 5347.9098908901215 seconds
# for 26x26 Execution time: 9406.609481334686 seconds