# -*- coding:utf-8 -*-
#三个数相乘最小

B = list(map(int,input().split()))
A = list(map(int,input().split()))
if len(A)<3:
    print(0)
else:
    max1 = 1
    max2 = 1
    max3 = 1
    min1 = 1
    min2 = 1
    for i in range(len(A)):
        if A[i]<min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]
        if A[i] > max1:
            max3 = max2
            max2 = max1
            max1 = A[i]
        elif A[i]> max2:
            max3 = max2
            max2 = A[i]
        elif A[i] > max3:
            max3 = A[i]
    res1 = max1*max2*max3
    res2 = max1*min1*min2
    res = max(res1,res2)
    print(res)
