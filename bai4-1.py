import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def compute(self,numProjects, maxResources, arr):
        previous_stage = [0 for x in range(maxResources)]
        current_stage = [0 for x in range(maxResources)]
        root = [0, 0, 0, None]
        current_node = None
        for i in range(maxResources):
            current_node = [1, i, arr[0][i], root]
            previous_stage[i] = current_node
        
        for i in range(2, numProjects):
            for j in range(maxResources):
                current_node = [i, j, 0, None]
                current_stage[j] = current_node
                for k in range(j + 1):
                    past_node = previous_stage[j - k]
                    profit = arr[i - 1][k]
                    cum_profit = profit + past_node[-2]
                    if cum_profit >= current_node[-2]:
                        current_node[-2] = cum_profit
                        current_node[-1] = past_node

            for j in range(maxResources):
                previous_stage[j] = current_stage[j]
        
        result = [numProjects + 1, maxResources - 1, 0, None]
        for i in range(maxResources):
            j = maxResources - 1 - i
            past_node = previous_stage[i]
            profit = arr[numProjects - 1][j]
            cum_profit = profit + past_node[-2]
            if cum_profit >= result[-2]:
                result[-2] = cum_profit
                result[-1] = past_node
                result[1] = j + past_node[1]

        return result[-2]
if __name__ == "__main__": 
    a = PTTK_GTNC()
    arr = [[3,5,7], [4,5,6],[3,6,7],[4,7,9]]
    numProjects = len(arr)
    maxResources = len(arr[0])
    print(a.compute(numProjects,maxResources,arr))