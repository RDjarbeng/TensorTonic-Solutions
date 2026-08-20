import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m, n = len(A), len(A[0])
    At =np.zeros((n, m))
    for i, row in enumerate(A):
        for j, column in enumerate(row):
            # print(j, column)
            At[j,i] = column
    return At
    pass
