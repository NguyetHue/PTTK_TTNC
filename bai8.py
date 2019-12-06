import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def JobScheduling(self, arr, arr1, t, n): 
        s = 0

        for i in range(n): 
            for j in range(n -1- i): 
                if arr[j][1] < arr[j + 1][1]: 
                    # print("arr["+str(j)+"][1] = "+str(arr[j][1] ), "arr["+str(j)+" + 1][1] = "+str(arr[j + 1][1]))
                    arr[j], arr[j + 1] = arr1[j + 1], arr1[j]
                    arr1[j], arr1[j + 1] = arr[j], arr[j+1]
        # print("array = ", arr )
        result = [False] * t 
        job = ['-1'] * t 
        for i in range(len(arr)):         
            for j in range(min(t - 1, arr[i][2] - 1), -1, -1): 
                if result[j] is False: 
                    result[j] = True
                    job[j] = arr[i][0] 
                    s += arr[i][1]
                    break
        print("bai 8 *************")
        print(job)
        print(s)
        return job, s
    def Bai8(self):   
        arr = []
        arr1 = []
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
                    arr1.append(line) 
                else:
                    n = line[0]
        A = np.array(arr)
        A1 = np.array(arr1)
        index = []
        for x in range(1,(len(A)+1)):
            index.append([x])
        # print(index)
        inputS = np.append(index,A,  axis=1)
        inputtemp = np.append(index,A1,  axis=1)
        # print(inputS)
        timeDealine = max(inputS[:,2])
        a.JobScheduling(inputS,inputtemp,timeDealine, n)
if __name__ == "__main__": 
    a = PTTK_GTNC()
    a.Bai8()