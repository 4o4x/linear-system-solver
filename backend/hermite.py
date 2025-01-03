import sympy
from sympy import gcdex,randMatrix
from tqdm import tqdm

def random_linear_diophantine_system(m, n):
    # Construct random integer system A*x = B
    # (We pick x, then define B = A*x.)
    x = randMatrix(n, 1, min=-100, max=100)
    A = randMatrix(m, n, min=-100, max=100)
    B = A * x
    return A, B, x


def hermite_normal_form(A):

    A = sympy.Matrix(A)
    U = sympy.eye(m)

    m, n = A.shape
    k = 0

    # Transformation to upper triangular form
    for j in range(n):
        for i in range(k + 1, m):
            if A[i, j] != 0:
                u,v,d = gcdex(A[k, j], A[i, j])
                B = u * A[k,:] + v * A[i,:]
                a = A[k, j] // d
                b = (A[i, j] // d)
                A[i,:] = a * A[i,:] -  b* A[k,:]
                A[k,:] = B

                B = u * U[k,:] + v * U[i,:]
                U[i,:] = a * U[i,:] - b * U[k,:]
                U[k,:] = B


        k += 1

    # Final reductions
    k = 0
    for j in range(n):
        if A[k, j] < 0:
            A[k,:] = -A[k,:]
            U[k,:] = -U[k,:]

        b = A[k, j]
        if b == 0:
            continue
        else:
            for i in range(k):
                q = A[i, j] // b
                A[i,:] =A[i,:] - (q * A[k,:])
                U[i,:] =U[i,:] - (q * U[k,:])
        k += 1
    return A,U

def linear_diophantine_system_solver(A, B):
    # Convert A, B to sympy
    A_sym = sympy.Matrix(A)
    B_sym = sympy.Matrix(B)

    # Compute hnf
    H,U = hermite_normal_form(A_sym.transpose())

    H_transpose = H.transpose()
    U_transpose = U.transpose()

    H_transpose_inv = H_transpose.inv()
    y = H_transpose_inv * B_sym
    x_sym = U_transpose*y


    return x_sym


def tester_hnf(func, m=15, n=15, total_tests=1000):

    fail = 0
    for i in tqdm(range(total_tests)):
        A, B, true_x = random_linear_diophantine_system(m, n)
        got_x = func(A, B)
        if got_x != true_x:
            fail += 1
            print(f"Test {i}: Failed. Expected: {true_x}, Got: {got_x}")

    print()
    print(f"[HNF Solver] Failed tests: {fail}/{total_tests}")


if __name__ == "__main__":
    # hnf,U = hermite_normal_form(A)
    # print("Hermite Normal Form of A:")

    # for i in range(hnf.rows):
    #     print(hnf.row(i))
    tester_hnf(linear_diophantine_system_solver,10,10,1000)
