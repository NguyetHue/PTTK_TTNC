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
            elif R.index(timeNow) == 0:
                timeNext = "4. Next landing time (t ="+str(timeNow)+"): " + str(R[R.index(timeNow)+1])
                timePrevious = "5. Previous landing time (t ="+str(timeNow)+" is time start) : " + str(-1)
                print(timeNext)
                print(timePrevious)
            elif R.index(timeNow) == len(R)-1:
                timeNext = "4. Next landing time (t ="+str(timeNow)+" is time end) : " + str(-1)
                timePrevious = "5. Previous landing time (t ="+str(timeNow)+" ) : " + str(R[R.index(timeNow)-1])
                print(timeNext)
                print(timePrevious)
            
            print(timeold)
        else:
            print("Time not found!!")
            a.checkNextPrevious(R)
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
            a.Bai1(k)
        #1. thời gian đăng ký hạ cánh sớm nhất còn lưu trong cấu trúc
        timeLandingEarliest = "2. the earliest landing time: " + str(R[0])
        #2. thời gian đăng ký hạ cánh trể nhất còn lưu trong cấu trúc
        timeLandingLatest = "3. the Latest landing time: " + str(R[len(R)-1])
        print(timeLandingEarliest)
        print(timeLandingLatest)
        a.checkNextPrevious(R)
    def cubes(self,a):
        arr = a[0]
        a.pop(0)
        for y in arr:
            temp = 0
            for x in a:
                if y in x:
                    x.remove(y)
                else:
        
                    print("y = ",y)
                   
        print(a)
        if len(a[0]) <= 1 and len(a[1]) <= 1:
            return arr[0]
        else:
            return -1
if __name__ == "__main__": 
    a = PTTK_GTNC()
    # a.Bai1(4)
    b = [[100,100,87],[13,100,6],[13,100,94]]
    print(a.cubes(b))