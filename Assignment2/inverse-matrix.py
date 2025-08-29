"""

 4- Calculate the inverse matrix of matrix A and check with the matrix product that both AA−1 and A−1 A produce a unit matrix with ones in diagonals
 and zeros elsewhere (the values will not be exactly 1 and 0 due to floating point error).
 A=( 1 2 3
    0 1 4
    5 6 0 )

"""

import numpy as np

A = np.array([
    [1,2,3],
    [0,1,4],
    [5,6,0]
 ])
inv_A = np.linalg.inv(A)
print(inv_A)
print("A * A-1\n",A@inv_A,"\n A-1 *A\n",inv_A@A)




