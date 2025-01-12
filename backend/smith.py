import sympy
from tqdm import tqdm
from sympy import Matrix, randMatrix,diag

def smith_normal_form(M):
    # Make sure M is a sympy Matrix
    A = M.copy()
    m, n = A.shape

    # Initialize S and T to identity matrices
    L = sympy.eye(m)
    R = sympy.eye(n)

    # Add alpha*rowj to rowi 
    def row_op(i, j, alpha):
        nonlocal A, L
        A[i, :] += alpha*A[j, :]
        L[i, :] += alpha*L[j, :]

    # Add alpha*colj to coli
    def col_op(i, j, alpha):
        nonlocal A, R
        A[:, i] += alpha*A[:, j]
        R[:, i] += alpha*R[:, j]

    # Iterate over smaller dimension
    r = min(m, n)
    # t indexes the diagonal position we are clearing
    while not A.is_diagonal():
        print("not diagonal")
        t = 0

        while t < r:
            # Step I: Pivot selection
            # Find the leftmost column col>=t with some nonzero below row t
            pivot_col = None
            for col in range(t, n):
                for row in range(t, m):
                    if A[row, col] != 0:
                        pivot_col = col
                        # print("pivot col selected:" + str(pivot_col))
                        break
                if pivot_col is not None:
                    break

            # If no pivot col found, we are done
            if pivot_col is None:
                break

            # Move the pivot up to row t (swap rows if needed)
            if A[t, pivot_col] == 0:
                for k in range(t+1, m):
                    if A[k, pivot_col] != 0:
                        # print("pivot is: " + str(A[k,pivot_col]))
                        A.row_swap(t, k)
                        L.row_swap(t, k)
                        break

            # Also swap pivot_col with t so pivot is at (t,t)
            if pivot_col != t:
                A.col_swap(t, pivot_col)
                R.col_swap(t, pivot_col)
                pivot_col = t

            # Step II: Improve the pivot so it divides entire pivot column
            improved = False
            while not improved:
                improved = True
                for row_below_pivot_index in range(t+1, m):
                    if A[t, t] != 0 and A[row_below_pivot_index, t] != 0 and (A[row_below_pivot_index, t] % A[t, t] != 0):
                        # print("improve pivot (col): " + str(t))
                        # gcd_val = sympy.gcd(A[t, t], A[row_below_pivot_index, t])
                        x, y, gcd_val = sympy.gcdex(A[t, t], A[row_below_pivot_index, t]) # Bezout: a*x + b*y = gcd
                        # row t <- x*row_t + y*row_below_pivot
                        row_t_new = x*A[t, :] + y*A[row_below_pivot_index, :]
                        alpha = -(A[row_below_pivot_index, t] // gcd_val)
                        beta = (A[t, t] // gcd_val)
                        # row_below_pivot_new <- alpha*row_t + beta*row_below_pivot
                        row_below_pivot_new = alpha*A[t, :] + beta*A[row_below_pivot_index, :]

                        A[t, :], A[row_below_pivot_index, :] = row_t_new, row_below_pivot_new

                        # same for L
                        L_t_new = x*L[t, :] + y*L[row_below_pivot_index, :]
                        L_row_below_pivot_new = alpha*L[t, :] + beta*L[row_below_pivot_index, :]
                        L[t, :], L[row_below_pivot_index, :] = L_t_new, L_row_below_pivot_new

                        improved = False
                        break

            # Now eliminate in the row by column ops
            improved_col = False
            while not improved_col:
                improved_col = True
                for col_right_pivot_index in range(t+1, n):
                    if A[t, t] != 0 and A[t, col_right_pivot_index] != 0 and (A[t, col_right_pivot_index] % A[t, t] != 0):
                        x, y, gcd_val = sympy.gcdex(A[t, t], A[t, col_right_pivot_index])
                        # col t <- x*col_t + y*col_right_pivot
                        col_t_new = x*A[:, t] + y*A[:, col_right_pivot_index]
                        alpha = -(A[t, col_right_pivot_index] // gcd_val)
                        beta = (A[t, t] // gcd_val)
                        col_right_pivot_new = alpha*A[:, t] + beta*A[:, col_right_pivot_index]

                        A[:, t], A[:, col_right_pivot_index] = col_t_new, col_right_pivot_new

                        # same for R
                        R_t_new = x*R[:, t] + y*R[:, col_right_pivot_index]
                        R_col_right_pivot_new = alpha*R[:, t] + beta*R[:, col_right_pivot_index]
                        R[:, t], R[:, col_right_pivot_index] = R_t_new, R_col_right_pivot_new

                        improved_col = False

                        break

            # Step III: Eliminate entries below pivot
            pivot_val = A[t, t]
            for row_below_pivot_index in range(t+1, m):
                if pivot_val != 0 and A[row_below_pivot_index, t] != 0:
                    q = A[row_below_pivot_index, t] // pivot_val
                    row_op(row_below_pivot_index, t, -q) 
             # Then eliminate entries on the pivot row
            pivot_val = A[t, t]
            if pivot_val != 0:
                for col_right_pivot_index in range(t+1, n):
                    if A[t, col_right_pivot_index] != 0:
                        q = A[t, col_right_pivot_index] // pivot_val
                        col_op(col_right_pivot_index, t, -q)     


            t += 1

    return (L, A, R)  # A is in Smith form (it might not be exact smith form but it is enough to solve linear diophantine systems)
def printMatrix(M):
    for i in range(M.rows):
        print(M.row(i))
def linear_diophantine_system_solver(A, B):
    # Convert A, B to sympy
    A_sym = sympy.Matrix(A)
    B_sym = sympy.Matrix(B)

    # Compute snf
    L,D,R = smith_normal_form(A)
    if not D.is_diagonal() :
        printMatrix(A_sym)
        printMatrix(D)
        exit()
    try:
        D_inv = D.inv()       # diagonal (Smith form) => easy to invert
    except:
        raise Exception("There is no unique solution to this system.")
    
    #   A x = B
    #   => L^-1 * D * R^-1 * x = B
    #   => D * (R^-1 x) = L * B
    #   => (R^-1 x) = D^-1 (L * B)
    #   => x = R * (D^-1 (L * B))

    x_sym = R * (D_inv * (L * B_sym))

    return x_sym  # Return the solution as a sympy Matrix


def tester_snf(func, m=15, n=15, total_tests=1000):
    def random_linear_diophantine_system(m, n):
        # Construct random integer system A*x = B
        # (We pick x, then define B = A*x.)
        x = randMatrix(n, 1, min=-100, max=100)
        A = randMatrix(m, n, min=-100, max=100)
        B = A * x
        return A, B, x

    fail = 0

    for i in tqdm(range(total_tests)):
        A, B, true_x = random_linear_diophantine_system(m, n)
        # print_linear_system(A,true_x,B)

        got_x = func(A, B)

        if got_x != true_x:
            fail += 1
            print(f"Test {i}: Failed. Expected: {true_x}, Got: {got_x}")

    print()
    print(f"[SNF Solver] Failed tests: {fail}/{total_tests}")

def print_linear_system(A,X,B):
    unknown_count = X.shape[0]
    row,col = A.shape
    for i in range(0,row):
        for j in range(0,unknown_count):
            if A[i, j] >= 0:
                print(f"+ {A[i, j]}x{j}", end=" ")
            else:
                print(f"- {abs(A[i, j])}x{j}", end=" ")
        print("= " +str(B[i]))
    # print unknowns
    for j in range(0,unknown_count):
        print("x"+str(j) +" = " + str(X[j]), end=", ")
    
def solve_system():
  #
#   A = [[-20, 79, -96, -59], [-65, 32, -66, 85], [63, -2, 10, 20], [56, 12, 57, -9]]
#   B = [-15790, 3282, -240, 967]
#   x = [-46, -44, 85, 86]

  # 
#   A = [[26, 45, 9, 17], [-34, 37, -74, 17], [-14, -27, -40, -75], [-28, 63, -31, 76]]
#   B =[800, -1320, -5616, 4774]
#   x = [-92, 42, 88, 30]

  A = [[78, -69, -20], [-38, -50, -98], [79, -32, 44]]  
  B =[[4721], [6072], [-463]]
  x = [[55], [21], [-94]]
  result = linear_diophantine_system_solver(A,B)
  expected = x
  got = result

  print("expected: " + str(expected))
  print("got: " + str(got))



if __name__ == "__main__":
    tester_snf(linear_diophantine_system_solver, m=30, n=30, total_tests=10)
    # A = [[9, 5, 4, 8], [-3, -5, 9, -7], [-6, 0, -9, -6], [-3, -5, 9, 5]]
    # b =[[-57], [-18], [69], [-90]]
    # L,A,R = smith_normal_form(Matrix(A))
    # print(A)
    # print(L)
    # print(R)
    # A = [[1,2,3],
    #      [4,5,6],
    #      [7,8,9]]

    # A = sympy.Matrix(A)
    # # L,A,R =smith_normal_form(A)
    # solve_system()
    

