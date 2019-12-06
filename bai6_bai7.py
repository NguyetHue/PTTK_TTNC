import sys
import numpy as np
from numpy import linalg as la
class PTTK_GTNC:
    def __init__(self):
        pass
    def knapsack(self,capacity, weights, values, items):
        grid = [[0] * (capacity + 1)]
        # print("grid: ", grid)
        for item in range(items):
            grid.append(grid[item].copy())

            for k in range(weights[item], capacity + 1):
                grid[item + 1][k] = max(grid[item][k], grid[item][k -weights[item]] + values[item])
                
        solution_value = grid[items][capacity]
        solution_weight = 0
        taken = []
        k = capacity
        for item in range(items, 0, -1):                                                                             
            # print("item= ", item)
            if grid[item][k] != grid[item - 1][k]:
                taken.append(item - 1)
                k -= weights[item - 1]
                solution_weight += weights[item - 1]
        # print(solution_value, taken)
        return solution_value, taken  
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
        print("bai 7 ****************")
        print ("fractions = ", fractions)
        print ("max_value =",max_value )
        return max_value, fractions
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
        print("bai 6 ****************")
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
if __name__ == "__main__": 
    a = PTTK_GTNC()
    a.Bai6()
    a.Bai7()