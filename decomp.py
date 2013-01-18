#from numpy import * #used for formatting of output only
from math import *


def choleskiDecomposition(matrix):
    '''
    Perform Choleski Decomposition of matrix.
    Does not use numpy.
    Assumes square matrix formatted as list of lists.
    '''
    
    lowerTriangle = matrix[:]
    upperTriangle = matrix[:]
    
    rows = len(matrix)
    
    lowerRow0 = [float(matrix[0][0])] #first row of lower triangle is standard 
    for i in range(1,rows):
        lowerRow0.append(0.0)
    lowerTriangle[0] = lowerRow0

    upperRow0 = [1.0] #first row of upper triangle is standard
    for i in range(1,rows):
        upperRow0.append(matrix[0][i]/float(lowerTriangle[0][0]))
    upperTriangle[0] = upperRow0

    for c in range(1,rows):
        lowerRow = [float(matrix[c][0])]
        upperRow = [0.0]
        for i in range(1,rows):
            # Lij = Aij - sum(Lik*Ukj) from k = 1 to j-1
            valueL = matrix[c][i]-lowerTriangle[c][i-1] * upperTriangle[i-1][c]
            lowerRow.append(float(valueL))

        if c != rows-1:
            lowerRow.pop()
            lowerRow.append(0.0)

        lowerTriangle[c] = lowerRow

        upperRow = [0.0]
        for i in range(1,rows):
            if len(upperRow) < c:
                upperRow.append(0.0)
            elif len(upperRow) == c:
                upperRow.append(1.0)
            else:
                #Uij = ( Aij - sum(Lik*Ukj) from k = 1 to j-1 )/Lii
                valueU = (matrix[c][i] - lowerTriangle[c][0] * upperTriangle[c-1][i])/float(lowerTriangle[c][c])
                upperRow.append(float(valueU))

        upperTriangle[c] = upperRow


    #print "Lower Choleski Triangle equals: \n"+ str(array(lowerTriangle))
    #print "Upper Choleski Triangle equals: \n"+ str(array(upperTriangle))

    print "Lower Choleski Triangle equals: \n"+ str((lowerTriangle))
    print "Upper Choleski Triangle equals: \n"+ str((upperTriangle))


