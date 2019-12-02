import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def Bai2(self):
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
        return(arr)
        def Bai3(self):
        A = [101,11,3,4,50,69,7,8,9,0]
        arrSort = []
        print("Enter K = ")
        k = input()   
        i = 0
        for x in A:
            i += 1
            if i ==1:
                arrSort.append(x)
            else:
                
          
        return(arr)


if __name__ == "__main__":
    a = PTTK_GTNC()
    a.Bai2()