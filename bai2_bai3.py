import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass  
    def Bai2(self):
        print("Bai 2--------------")
        A = [101,11,3,101,4,50,69,7,4,8,9,0]
        arr = []
        i = 0
        for x in A:
            i += 1
            if i == 1:
                arr.append(x) 
            else:
                    if x in arr:
                        print("remove pt : ", x)
                    else:
                        arr.append(x) 
        print("Result arrays do not coincide: ", arr)
        return(arr)
    def Bai3(self):
        print("Bai 3--------------")
        A = [101,11,3,4,50,69,7,8,9,0]
        arrSort = []
        k = int(input("Enter K =")) 
        while A:
            temp = A[0] 
            for x in A: 
                if x > temp:
                    temp = x
            arrSort.append(temp)
            A.remove(temp) 
        if k > len(arrSort):
            return ("K > length array ==> not value")
        else:
            print(arrSort)
            print("k = ", k )
            print('Value = ' + str(arrSort[k-1]))
            return ('Value = ' + str(arrSort[k-1])) 
if __name__ == "__main__": 
    a = PTTK_GTNC()
    a.Bai2()
    a.Bai3()