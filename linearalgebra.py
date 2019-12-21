#Operation on Matrix using numpy and linalg
# Importing numpy as np
import numpy as np
import numpy.matlib
a = np.array([[6, 1, 1],
             [4, -2, 5],
             [2, 8, 7]])
b=np.array([[1,2,3],
	   [4,5,6],
           [6,8,1]])
from scipy import linalg
# Rank of a matrix
print "Rank of a:", np.linalg.matrix_rank(a)
# Trace of matrix a
print "\nTrace of a:", np.trace(a)
# Determinant of a matrix a
print "\nDeterminant of a:", np.linalg.det(a)
# Inverse of matrix A
print "\nInverse of a:\n", np.linalg.inv(a)
#Transpose 
print "Transpose of matrix a:\n",a.transpose()
#Eigen values
print "Eigen values of matrix a\n",linalg.eig(a)
# Addition of two array
print "Addition of two matrix:\n" ,np.add(a,b)
# Subtraction of two Matrix
print "Subtraction of two matrix:\n",np.subtract(a,b)
# Multiplication
print "Multiplication of two matrix:\n",np.dot(a,b)
#Division
print "Division of two matrix:\n",np.divide(a,b)



