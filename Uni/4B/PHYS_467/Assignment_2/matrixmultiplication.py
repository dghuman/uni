# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:50:31 2019

@author: Dilraj
"""
import cmath,numpy,math

T = [[1. ,0.],
     [0, complex(1./math.sqrt(2),1./math.sqrt(2))]]
cZ = [[1., 0., 0., 0.],
      [0., 1., 0., 0.],
      [0., 0., 1., 0.],
      [0., 0., 0., -1.]]
K = [[(1/math.sqrt(2)), (1/math.sqrt(2))*complex(0,1)], [(1/math.sqrt(2))*complex(0,1), (1/math.sqrt(2))]]
Z = [[1., 0,],
     [0., -1.]]
resultF = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# Multiply Matrices
def Mult(X,Y):
    result = numpy.zeros((int(len(X)),int(len(X[0]))),dtype="complex")
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

#Powers of Matrices
def Power(M, n):
    result = M
    for i in range(n-1):
        result = Mult(result,M)
    return result

MaybeH = Mult(K,Mult(Power(T,6),K))
A = Power(K,2)
B = Power(T,2)
C = Mult(A,B)
D = Mult(B,A)
for r in Mult(C,Mult(K,D)):
    print r
print("We want: ",1./math.sqrt(2))


