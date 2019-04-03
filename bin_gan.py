# -*- coding:utf-8 -*-
##饥饿值的题目，小饼干，

def cal_hug(a, temp_hug):
    temp = []
    for i in range(len(temp_hug)):
        if temp_hug[i] <= a:
            a -=temp_hug[i]
        else:
            temp.append(temp_hug[i])
    return (a,temp)
if __name__=='__main__':
    # n,m = list(map(int,input().split()))
    # hungry_vl = list(map(int,input().split()))
    n = 2
    m = 5
    hungry_vl=[5,6,10,20,30]
    # A = []
    A = [[4,34,0],[3,35,1]]
    # for i in range(n):
    #     fit_vl,hungry_now = list(map(int,input().split()))
    #     A.append((fit_vl,hungry_now,i))

    hungry_vl.sort(reverse=True)
    A.sort(key = lambda x:x[0],reverse=True)

    res = []
    temp_hug = hungry_vl

    temp_h =0
    for i in range(n):
        temp_h,temp_hug = cal_hug(A[i][1], temp_hug)
        res.append((A[i][2], temp_h))

    res.sort(key=lambda x: x[0])

    for i in range(len(res)):
        print(res[i][1])
