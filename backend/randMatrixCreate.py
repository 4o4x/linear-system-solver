import json
import sympy as sp
import numpy as np
from sympy import randMatrix

def random_matrix(size):
    matrix = [[np.random.randint(-10, 10) for _ in range(size)] for _ in range(size)]    
    return matrix

# Save matrices to a JSON file
def save_matrices_to_json(filename, matrices):
    with open(filename, 'w') as file:
        json.dump(matrices, file)

# Load matrices from a JSON file
def load_matrices_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":

    # Save the matrices
    size = 3
    for size in range(2,31):
        matrices = []
        for i in range(0,1000):
            randomMatrix = random_matrix(size)

            matrices.append(randomMatrix)
        save_matrices_to_json("matrices/"+str(size) + 'x' + str(size) + '_matrices.json', matrices)

    # # Load the matrices back
    # loaded_matrices = load_matrices_from_json('matrices.json')

    # # Print loaded matrices
    # for idx, matrix in enumerate(loaded_matrices, 1):
    #     print(f"Matrix {idx}:")
    #     smt = sp.Matrix(matrix)
    #     print(smt)

