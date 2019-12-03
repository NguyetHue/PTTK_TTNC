import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def checkTime(self, k):
        tt = input()
        if k > int(tt):
            print("Registration time has expired !")
            print("Register new time: ")
            a.checkTime(k)
        print("vc ==", tt)
        return int(tt)
    def Bai1(self): 
        R = [37,41,46,49,56]
        k = 3
        print("Enter time: ")
        t = a.checkTime(R[0])
        print("t====", t)
        kq = 1
        temp = 0
        for x in R:
            ss = x-t 
            # print("ss = ", ss)
            if ss < k and ss > -k:          
              kq = 0
              temp = x 
            else:
                if x > t:
                   temp = x            
        if kq == 1:
            print("Registration successful!") 
            if temp != 0:
                # print(R.index(temp))
                R.insert(R.index(temp),t)
            else:
                R.insert(len(R),t)
            print(R)  
        elif kq == 0:
            print("Registration failed!") 
        #1. thời gian đăng ký hạ cánh sớm nhất còn lưu trong cấu trúc
        timeLandingEarliest = "the earliest landing time: " + str(R[0])
        #2. thời gian đăng ký hạ cánh trể nhất còn lưu trong cấu trúc
        timeLandingLatest = "the Latest landing time: " + str(R[len(R)-1])
        print(timeLandingLatest)
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
            k = int(k)   
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
                return ('Value = ' + str(arrSort[k-1])) 
    def Bai5(self):
        arr = []
        result = []
        s = 0
        i = 0
        with open('bai5.txt') as file_data:
            for line in file_data:
                i += 1
                if i != 1:
                    line = line.strip()
                    line = list(line.split())
                    arr.append(list(map(int, line))) 
        print(arr)
        a.maxSum(arr, 5)
  
    def maxSum(self, dA, n): 
        arr =[]
        arrLable = []
        arrLable = dA
        arr.append(arrLable[0][0])
        if n > 1: 
            dA[1][0] = dA[1][0]+dA[0][0] 
            print( "dA[1][0] = ", dA[1][0] )
            dA[1][1] = dA[1][1]+dA[0][0] 
            print( "dA[1][1] = ", dA[1][1] ) 
            if dA[1][0] > dA[1][1]:
                arr.append(arrLable[1][0])
            else:
                arr.append(arrLable[1][1])
        for i in range(2, n): 
            if dA[i][0]+dA[i-1][0] >= dA[i][0]+dA[i-1][1]: 
                dA[i][0] = dA[i][0]+dA[i-1][0] 
            else: 
                dA[i][0] = dA[i][0]+dA[i-1][1]
            print("dA["+str(i)+"][0] = ",dA[i][0])
            dA[i][i] = dA[i][i] + dA[i-1][i-1] 
            print("dA["+str(i)+"][" +str(i)+ "]  = ",dA[i][i])
            for j in range(1, i): 
                if dA[i][j]+dA[i-1][j-1] >= dA[i][j]+dA[i-1][j]: 
                    dA[i][j] = dA[i][j] + dA[i-1][j-1] 
                    print("dA["+str(i)+"][" +str(j)+ "]  = ",dA[i][j])
                else: 
                    dA[i][j] = dA[i][j]+dA[i-1][j] 
                    print("dA["+str(i)+"][" +str(j)+ "]  = ",dA[i][j])
        print (max(dA[n-1])) 
        print (arr) 


if __name__ == "__main__":
    a = PTTK_GTNC()
    # res =  a.Bai3()
    # print(res)
    a.Bai5()