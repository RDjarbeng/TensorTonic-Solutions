import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m, n = len(A), len(A[0])
    # print(m, n)
    At =np.zeros((n, m))
    # print(At.shape)
    for i, row in enumerate(A):
        # print(i)
        # print(row)
        for j, column in enumerate(row):
            # print(j, column)
            At[j,i] = column
    # print('At', At)
    return At
    pass
