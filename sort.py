'''
--------------------------
'''
'''冒泡排序
'''

def BubbleSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range (0,n):
        for j in range(0,n-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=BubbleSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
'''
--------------------------
'''
'''简单选择排序
'''
def SelectSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range(0,n-1):
        minIndex=i
        for j in range(i+1,n):#比较一遍，记录索引不交换
            if ls[j]<ls[minIndex]:
                minIndex=j
        if minIndex!=i:#按索引交换
            ls[minIndex],ls[i]=ls[i],ls[minIndex]
    return ls

x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in y:
    arr.append(int(i))
arr=SelectSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
'''
--------------------------
简单插入排序
'''
def InsertSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range(1,n):
        j=i
        target=ls[i]            #每次循环的一个待插入的数
        while j>0 and target<ls[j-1]:       #比较、后移，给target腾位置
            ls[j]=ls[j-1]
            j=j-1
        ls[j]=target            #把target插到空位
    return ls

x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=InsertSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
'''
--------------------------
堆排序
'''
def  HeapSort(ls):
    def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
        temp=arr[start]
        son=2*start+1
        while son<=end:
            if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                son+=1
            if temp>=arr[son]:       #判断是否为大顶堆
                break
            arr[start]=arr[son]     #子节点上移
            start=son                     #继续向下比较
            son=2*son+1
        arr[start]=temp             #将原堆顶插入正确位置
#######
    n=len(ls)
    if n<=1:
        return ls
    #建立大顶堆
    root=n//2-1    #最后一个非叶节点（完全二叉树中）
    while(root>=0):
        heapadjust(ls,root,n-1)
        root-=1
    #掐掉堆顶后调整堆
    i=n-1
    while(i>=0):
        (ls[0],ls[i])=(ls[i],ls[0])  #将大顶堆堆顶数放到最后
        heapadjust(ls,0,i-1)    #调整剩余数组成的堆
        i-=1
    return ls
#########
x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=HeapSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')

'''
--------------------------
快速排序
'''
def QuickSort(ls):
    def partition(arr,left,right):
        key=left         #划分参考数索引,默认为第一个数，可优化
        while left<right:
            while left<right and arr[right]>=arr[key]:
                right-=1
            while left<right and arr[left]<=arr[key]:
                left+=1
            (arr[left],arr[right])=(arr[right],arr[left])
        (arr[left],arr[key])=(arr[key],arr[left])
        return left

    def quicksort(arr,left,right):   #递归调用
        if left>=right:
            return
        mid=partition(arr,left,right)
        quicksort(arr,left,mid-1)
        quicksort(arr,mid+1,right)
    #主函数
    n=len(ls)
    if n<=1:
        return ls
    quicksort(ls,0,n-1)
    return ls

x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=QuickSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')

'''
--------------------------
希尔排序
'''

def ShellSort(ls):
    def shellinsert(arr,d):
        n=len(arr)
        for i in range(d,n):
            j=i-d
            temp=arr[i]             #记录要出入的数
            while(j>=0 and arr[j]>temp):    #从后向前，找打比其小的数的位置
                arr[j+d]=arr[j]                 #向后挪动
                j-=d
            if j!=i-d:
                arr[j+d]=temp
    n=len(ls)
    if n<=1:
        return ls
    d=n//2
    while d>=1:
        shellinsert(ls,d)
        d=d//2
    return ls


x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=ShellSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')

'''
--------------------------
归并排序
'''
def MergeSort(ls):
    #合并左右子序列函数
    def merge(arr,left,mid,right):
        temp=[]     #中间数组
        i=left          #左段子序列起始
        j=mid+1   #右段子序列起始
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=right:
            temp.append(arr[j])
            j+=1
        for i in range(left,right+1):    #  !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i]=temp[i-left]
    #递归调用归并排序
    def mSort(arr,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        mSort(arr,left,mid)
        mSort(arr,mid+1,right)
        merge(arr,left,mid,right)

    n=len(ls)
    if n<=1:
        return ls
    mSort(ls,0,n-1)
    return ls

x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=MergeSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')


'''
---------------------------------
计数排序
'''
def CountSort(ls):
    n=len(ls)
    num=max(ls)
    count=[0]*(num+1)
    for i in range(0,n):
        count[ls[i]]+=1
    arr=[]
    for i in range(0,num+1):
        for j in range(0,count[i]):
            arr.append(i)
    return arr


x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=CountSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')



'''
---------------------------
桶排序
'''
def BucketSort(ls):
    ##############桶内使用快速排序
    def QuickSort(ls):
        def partition(arr,left,right):
            key=left         #划分参考数索引,默认为第一个数，可优化
            while left<right:
                while left<right and arr[right]>=arr[key]:
                    right-=1
                while left<right and arr[left]<=arr[key]:
                    left+=1
                (arr[left],arr[right])=(arr[right],arr[left])
            (arr[left],arr[key])=(arr[key],arr[left])
            return left

        def quicksort(arr,left,right):   #递归调用
            if left>=right:
                return
            mid=partition(arr,left,right)
            quicksort(arr,left,mid-1)
            quicksort(arr,mid+1,right)
        #主函数
        n=len(ls)
        if n<=1:
            return ls
        quicksort(ls,0,n-1)
        return ls
    ######################
    n=len(ls)
    big=max(ls)
    num=big//10+1
    bucket=[]
    buckets=[[] for i in range(0,num)]
    for i in ls:
        buckets[i//10].append(i)     #划分桶
    for i in buckets:                       #桶内排序
        bucket=QuickSort(i)
    arr=[]
    for i in buckets:
        if isinstance(i, list):
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    for i in range(0,n):
        ls[i]=arr[i]
    return ls

x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=BucketSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')


'''
-----------------------------
基数排序
'''
import math
def RadixSort(ls):
    def getbit(x,i):       #返回x的第i位（从右向左，个位为0）数值
        y=x//pow(10,i)
        z=y%10
        return z
    def CountSort(ls):
        n=len(ls)
        num=max(ls)
        count=[0]*(num+1)
        for i in range(0,n):
            count[ls[i]]+=1
        arr=[]
        for i in range(0,num+1):
            for j in range(0,count[i]):
                arr.append(i)
        return arr
    Max=max(ls)
    for k in range(0,int(math.log10(Max))+1):             #对k位数排k次,每次按某一位来排
        arr=[[] for i in range(0,10)]
        for i in ls:                 #将ls（待排数列）中每个数按某一位分类（0-9共10类）存到arr[][]二维数组（列表）中
            arr[getbit(i,k)].append(i)
        for i in range(0,10):         #对arr[]中每一类（一个列表）  按计数排序排好
            if len(arr[i])>0:
                arr[i]=CountSort(arr[i])
        j=9
        n=len(ls)
        for i in range(0,n):     #顺序输出arr[][]中数到ls中，即按第k位排好
            while len(arr[j])==0:
                j-=1
            else:
                ls[n-1-i]=arr[j].pop()
    return ls

x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=RadixSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
