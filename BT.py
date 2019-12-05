import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def checkTime(self, k):
        t = input()
        if k > int(t):
            print("Registration time has expired !")
            print("Register new time: ")
            return a.checkTime(k)
        else:
            return int(t)
    def checkNextPrevious(self, R):
        print("Enter time now : ")
        timeNow = input()
        timeNow = int(timeNow)
        timeNext =""
        timePrevious=""
        timeold=""
        if timeNow in R:
            # 6. có bao nhiêu chuyến bay đã đăng ký từ thời điểm t trờ về trước
            timeold =  "6. Number flight landing before time (t ="+str(timeNow)+" ) : " + str(R.index(timeNow))
            
            if R.index(timeNow) < len(R)-1 and R.index(timeNow) != 0:
                # 4. Trả về thời điểm hạ cánh kế tiếp của thời điểm t cho trước, nếu t là giá trị lớn nhất trong cấu trúc thì -1 được trả về
                timeNext = "4. Next landing time (t ="+str(timeNow)+"): " + str(R[R.index(timeNow)+1])
                # 5. Trả về thời điểm hạ cánh trước đó của thời điểm t cho trước, nếu t là giá trị nhỏ nhất trong cấu trúc thì -1 được trả về.
                timePrevious = "5. Previous landing time (t ="+str(timeNow)+" ) : " + str(R[R.index(timeNow)-1])

                print(timeNext)
                print(timePrevious)
            elif R.index(timeNow) == len(R)-1:
                timeNext = "4. Next landing time (t ="+str(timeNow)+" is time end) : " + str(-1)
                timePrevious = "5. Previous landing time (t ="+str(timeNow)+" ) : " + str(R[R.index(timeNow)-1])
                print(timeNext)
                print(timePrevious)
            elif R.index(timeNow) == 0:
                timeNext = "4. Next landing time (t ="+str(timeNow)+"): " + str(R[R.index(timeNow)+1])
                timePrevious = "5. Previous landing time (t ="+str(timeNow)+" is time start) : " + str(-1)
                print(timeNext)
                print(timePrevious)
            print(timeold)
        else:
            print("Time not found!!")
            a.checkNextPrevious(R)
    def knapsack(self,capacity, weights, values, items):
        grid = [[0] * (capacity + 1)]
        # print("grid: ", grid)
        for item in range(items):
            grid.append(grid[item].copy())
            print("grid: ", grid)
            print("grid: ", grid)
            for k in range(weights[item], capacity + 1):
                grid[item + 1][k] = max(grid[item][k], grid[item][k -weights[item]] + values[item])
        # print("grid: ", grid)
        solution_value = grid[items][capacity]
        solution_weight = 0
        taken = []
        k = capacity
        for item in range(items, 0, -1):
            if grid[item][k] != grid[item - 1][k]:
                # print("item: ", item)
                taken.append(item - 1)
                k -= weights[item - 1]
                solution_weight += weights[item - 1]
        print(grid)
        return solution_value, taken  
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
    def fractional_knapsack(self,value, weight, capacity):
        index = list(range(len(value)))
        ratio = [v/w for v, w in zip(value, weight)]
        index.sort(key=lambda i: ratio[i], reverse=True)
        max_value = 0
        fractions = [0]*len(value)
        for i in index:
            if weight[i] <= capacity:
                fractions[i] = 1
                max_value += value[i]
                capacity -= weight[i]
            else:
                fractions[i] = capacity/weight[i]
                max_value += value[i]*capacity/weight[i]
                break
        print (fractions)
        print (max_value)
        return max_value, fractions
    def JobScheduling(self, arr, t, n): 
        s = 0
        print(arr[0][1])
        for i in range(n): 
            for j in range(n - 1 - i): 
                if arr[j][1] < arr[j + 1][1]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        result = [False] * t 
        job = ['-1'] * t 
        for i in range(len(arr)): 
            for j in range(min(t - 1, arr[i][2] - 1), -1, -1): 
                if result[j] is False: 
                    result[j] = True
                    job[j] = arr[i][0] 
                    s += arr[i][1]
                    break
        print(job)
        print(s) 
    def Bai1(self, k): 
        R = [37, 41, 46, 49, 56] 
        print ("Enter time: ")
        t = a.checkTime(R[0])
        kq = 1
        temp = 0
        for x in R:
            ss = x-t # ss khoảng thời gian giữa đăng ký mới và csdl
            if ss < k and ss > -k:          
              kq = 0
              temp = x 
            else:
                if x > t:
                   temp = x            
        if kq == 1:
            print("Registration successful!") 
            if temp != 0:
  
                R.insert(R.index(temp),t)
            else:
                R.insert(len(R),t)
            print(R)  
        elif kq == 0:
            print("Registration failed!") 
        #1. thời gian đăng ký hạ cánh sớm nhất còn lưu trong cấu trúc
        timeLandingEarliest = "2. the earliest landing time: " + str(R[0])
        #2. thời gian đăng ký hạ cánh trể nhất còn lưu trong cấu trúc
        timeLandingLatest = "3. the Latest landing time: " + str(R[len(R)-1])
        print(timeLandingEarliest)
        print(timeLandingLatest)
        a.checkNextPrevious(R)
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
    def Bai6(self):
        arr = []
        M = 0
        n = 0
        i = 0 
        with open('bai6.txt') as file_data:
            for line in file_data:
                i += 1
                line = line.strip()
                line = list(line.split())
                line = list(map(int, line))
                if i != 1:
                    arr.append(line) 
                else:
                    M = line[0]
                    n = line[1]
        A = np.array(arr)
        knapsackresult= []
        result = []
        knapsackresult = a.knapsack(M,A[:,0],A[:,1], n)
        for x in range(len(A[:,0])):
            if x in knapsackresult[1]:
                result.append(1)
            else:
                result.append(0)
        print(result)
        print(knapsackresult[0])
    def Bai7(self):
        arr = []
        M = 0
        n = 0
        i = 0 
        with open('bai6.txt') as file_data:
            for line in file_data:
                i += 1
                line = line.strip()
                line = list(line.split())
                line = list(map(int, line))
                if i != 1:
                    arr.append(line) 
                else:
                    M = line[0]
                    n = line[1]
        A = np.array(arr)
        a.knapsackresult = a.fractional_knapsack(A[:,1],A[:,0],M)
    
    def Bai8(self):   
        arr = []
        inputS = []
        n = 0
        i = 0 
        with open('bai8.txt') as file_data:
            for line in file_data:
                i += 1
                line = line.strip()
                line = list(line.split())
                line = list(map(int, line))
                if i != 1:
                    arr.append(line) 
                else:
                    n = line[0]
        A = np.array(arr)
        index = []
        for x in range(1,(len(A)+1)):
            index.append([x])
        print(index)
        inputS = np.append(index,A,  axis=1)
        print(inputS)
        a.JobScheduling(inputS, 3, n)
if __name__ == "__main__": 
    a = PTTK_GTNC()
    a.Bai6()