import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def maxSum(self, dA, n): 
        arr =[]
        # arrLable = insert(dA)
        if n > 1: 
            dA[1][0] = dA[1][0]+dA[0][0] 
            # print( "dA[1][0] = ", dA[1][0] )
            dA[1][1] = dA[1][1]+dA[0][0] 
            # print( "dA[1][1] = ", dA[1][1] ) 
        for i in range(2, n): 
            if dA[i][0]+dA[i-1][0] >= dA[i][0]+dA[i-1][1]: 
                dA[i][0] = dA[i][0]+dA[i-1][0] 
            else: 
                dA[i][0] = dA[i][0]+dA[i-1][1]
            # print("dA["+str(i)+"][0] = ",dA[i][0])
            dA[i][i] = dA[i][i] + dA[i-1][i-1] 
            # print("dA["+str(i)+"][" +str(i)+ "]  = ",dA[i][i])
            for j in range(1, i): 
                if dA[i][j]+dA[i-1][j-1] >= dA[i][j]+dA[i-1][j]: 
                    dA[i][j] = dA[i][j] + dA[i-1][j-1] 
                    # print("dA["+str(i)+"][" +str(j)+ "]  = ",dA[i][j])
                else: 
                    dA[i][j] = dA[i][j]+dA[i-1][j] 
                    # print("dA["+str(i)+"][" +str(j)+ "]  = ",dA[i][j])
        return [max(dA[n-1]),dA]
    def Bai5(self):
        arr = []
        arrold = []
        col = 0
        i = 0
        with open('bai5.txt') as file_data:
            for line in file_data:
                i += 1
                if i != 1:
                    line = line.strip()
                    line = list(line.split())
                    arr.append(list(map(int, line))) 
                    arrold.append(list(map(int, line))) 
                else:
                    col = int(line)
        resultArray =a.maxSum(arr,col)
        indexs = []
        indexs1= []
        j = 0
        for x in reversed(resultArray[1]):
            j += 1
            m = resultArray[1].index(x)
            # for y in reversed(arrold):
            if j == 1:
                indexs.append(arrold[m][x.index(max(x))])
                indexs1.append(max(x))
            else:
                # print(arrold[m])
                v = arrold[m][x.index(indexs1[j-2]-indexs[j-2])]
                indexs.append(v)
                indexs1.append(indexs1[j-2]-indexs[j-2])
        print(indexs[::-1])
        print(resultArray[0])  
if __name__ == "__main__": 
    a = PTTK_GTNC()
    a.Bai5()