from hermite import hermite_normal_form
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
        H, U = hermite_normal_form(smt)
        # print(H)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"for {size}x{size} Execution time: {execution_time} seconds")

# for 3x3 Execution time: 2.364091396331787 seconds
# for 4x4 Execution time: 4.905017137527466 seconds
# for 5x5 Execution time: 8.928385257720947 seconds
# for 6x6 Execution time: 13.989642858505249 seconds
# for 7x7 Execution time: 19.894989728927612 seconds
# for 8x8 Execution time: 29.36741542816162 seconds
# for 9x9 Execution time: 39.035167932510376 seconds
# for 10x10 Execution time: 51.88647770881653 seconds
# for 11x11 Execution time: 64.17065668106079 seconds
# for 12x12 Execution time: 81.82034969329834 seconds
# for 13x13 Execution time: 102.75686478614807 seconds
# for 14x14 Execution time: 121.86689233779907 seconds
# for 15x15 Execution time: 146.11681866645813 seconds
# for 16x16 Execution time: 174.47412824630737 seconds
# for 17x17 Execution time: 204.48312759399414 seconds
# for 18x18 Execution time: 239.81779623031616 seconds
# for 19x19 Execution time: 276.5863924026489 seconds
# for 20x20 Execution time: 326.2010054588318 seconds
# for 21x21 Execution time: 383.6619641780853 seconds
# for 22x22 Execution time: 474.0774657726288 seconds
# for 23x23 Execution time: 565.2949502468109 seconds
# for 24x24 Execution time: 712.5214202404022 seconds
# for 25x25 Execution time: 962.9764354228973 seconds
# for 26x26 Execution time: 1355.8427875041962 seconds
# for 27x27 Execution time: 4287.151536226273 seconds
# for 28x28 Execution time: 3402.060627222061 seconds
# for 29x29 Execution time: 7501.912122964859 seconds