import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def bai4(self,numCourse, maxdate, arr):
        arrpoint = []
        arrtemp = []
        arrs = []
        # print("numcourse= ", numCourse)
        date = maxdate//numCourse
        if date:
            arrpoint.append(sum(arr[:,date]))
            maxdate = maxdate - numCourse*date
            if maxdate > 0:
                # print (maxdate)
                for i in reversed(range(0,numCourse)):
                    for j in range(i):
                        arrtemp.append(arr[i][date+1]+arr[j][date+1])
                        arrs.append([arr[i][0],arr[j][0]])
                arrs = arrs[arrtemp.index(max(arrtemp))]
                s = max(arrtemp)
                for i in range(numCourse):
                    if i in arrs:
                        print("course "+str(i+1)+" = "+str(date+1)+" date")
                    else:
                        print("course "+str(i+1)+" = "+str(date)+" date")
                        s += arr[i][1]
                print("sum scores =", s)
        
    # def arrangeSchedule(self,numCourse, maxResources, arr):
    #     previous_stage = [0 for x in range(maxResources)]
    #     current_stage = [0 for x in range(maxResources)]
    #     root = [0, 0, 0, None]
    #     current_node = None
    #     for i in range(maxResources):
    #         current_node = [1, i, arr[0][i], root]
    #         # print("current_node = ", current_node)
    #         previous_stage[i] = current_node
    #         # print("previous_stage["+str(i)+"] = ", previous_stage)
        
    #     for i in range(2, numCourse):
    #         for j in range(maxResources):
    #             current_node = [i, j, 0, None]
    #             # print("current_node1111 = ", current_node)
    #             current_stage[j] = current_node
    #             # print("previous_stage["+str(i)+"] = ", previous_stage)
    #             for k in range(j + 1):
    #                 past_node = previous_stage[j - k]
    #                 profit = arr[i - 1][k]
    #                 cum_profit = profit + past_node[-2]
    #                 if cum_profit >= current_node[-2]:
    #                     current_node[-2] = cum_profit
    #                     current_node[-1] = past_node

    #         for j in range(maxResources):
    #             previous_stage[j] = current_stage[j]
        
    #     result = [numCourse + 1, maxResources - 1, 0, None]
    #     for i in range(maxResources):
    #         j = maxResources - 1 - i
    #         past_node = previous_stage[i]
    #         profit = arr[numCourse - 1][j]
    #         cum_profit = profit + past_node[-2]
    #         if cum_profit >= result[-2]:
    #             result[-2] = cum_profit
    #             result[-1] = past_node
    #             result[1] = j + past_node[1]
    #     print(result)
    #     return result[-2]
if __name__ == "__main__": 
    a = PTTK_GTNC()
    arr = np.array([[0,3,5,7], [1,4,5,6],[2,3,6,7],[3,4,7,9]])
    arr1 = np.array([[3,5,7], [4,5,6],[3,6,7],[4,7,9]])
    numCourse = len(arr)
    maxResources = len(arr[0])
    # print("Time course: ", a.arrangeSchedule(numCourse,maxResources,arr))
    maxdate= 6
    a.bai4(numCourse,maxdate,arr)