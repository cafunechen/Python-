def maopao(s):
    if len(s)<=1:
        return s
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]> s[j]:
                s[i],s[j] = s[j],s[i]
    return s

# def xuanze(s):
#     if len(s)<=1:
#         return s
#     for i in range(len(s)-1):
#         minindex = i
#         for j in range(i+1,len(s)):
#             if s[j]<s[minindex]:
#                 minindex = j
#         if minindex !=i:
#             s[i],s[minindex] = s[minindex],s[i]
#     return s

#
# def charu(s):
#     n = len(s)
#     for i in range(1,n):
#         j = i
#         target = s[i]
#         while s[j-1]>target and j>0:
#             s[j] = s[j-1]
#             j -=1
#         s[j] = target
#     return s

# def xier(s):
#     # import math
#     gap =1
#     #寻找动态定义间隔最大值
#     while gap<(len(s)/3):
#         gap = gap*3+1
#     while gap>0:
#         for i in range(gap,len(s)):
#             temp = s[i]
#             j = i-gap
#             while j>=0 and s[j]> temp:
#                 s[j+gap] = s[j]
#                 j-=gap
#             if j!=i-gap:
#                 s[j+gap] = temp
#         gap = (gap-1)//3
#         #这里一定要//，因为要取整 0/3=0.0，默认为浮点型
#         #0.0>0是false
#     return s


# def guibing(s):
#     def mergesort(s):
#         if len(s)<2:
#             return s
#         middle = len(s)//2
#         left,right = s[0:middle],s[middle:]
#         #递归
#         return merge(mergesort(left),mergesort(right))
#
#     def merge(left,right):
#         res = []
#         while left and right:
#             if left[0]<=right[0]:
#                 res.append(left.pop(0))
#             else:
#                 res.append(right.pop(0))
#         while left:
#             res.append(left.pop(0))
#         while right:
#             res.append(right.pop(0))
#         return  res
#     return mergesort(s)
#

            # def heap_sort(elems):
            #     def siftdown(elems, e, begin, end): #向下筛选
            #         i, j = begin, begin*2+1 #j为i的左子结点
            #         while j < end:
            #             if j+1 < end and elems[j] > elems[j+1]: #如果左子结点大于右子结点
            #                 j += 1                              #则将j指向右子结点
            #             if e < elems[j]: #j已经指向两个子结点中较小的位置，
            #                 break        #如果插入元素e小于j位置的值，则为3者中最小的
            #             elems[i] = elems[j] #能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父结点位置
            #             i, j = j, j*2+1 #更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
            #         elems[i] = e #如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父结点
            #                      #或者位置i已经更新到叶结点位置，则将e赋给这个叶结点。
            #
            #     end = len(elems)
            #     for i in range(end//2-1, -1, -1): #构造堆序。
            #         siftdown(elems, elems[i], i, end)
            #     for i in range ((end-1), 0,-1): #进行堆排序.i最后一个值为1，不需要到0
            #         print(elems)
            #         e = elems[i] #将末尾元素赋给e
            #         elems[i] = elems[0] #交换堆顶与最后一个元素
            #         siftdown(elems, e, 0, i)
            #
            #     return(elems)
            #
            # if __name__=="__main__":
            #     print(heap_sort([5,6,8,1,2,4,9]))
# def quick_sort(s):
#     def left_right(s,left,right):
#         stand = s[left]
#         while left<right:
#             while left<right and s[right]>=stand:
#                 right-=1
#             s[left] = s[right]
#             while left<right and s[left]<=stand:
#                 left+=1
#             s[right] = s[left]
#         s[left] = stand
#         return left
#     def sort(s,left,right):
#         if left<right:
#             stand = left_right(s,left,right)
#
#             sort(s,left,stand-1)
#             sort(s,stand+1,right)
#         return s
#     l = len(s)
#     sort(s,0,l-1)
#     return s



# def dui(s):
#     def zuidadui(s,father,begin,end):
#         i = begin
#         j = begin*2+1 #左子节点
#         while j <end:
#             if j+1<end and s[j+1]>s[j]:
#                 j+=1
#             if father>s[j]:
#                 break#不更新i，j，因为父节点是最大的，不用调整顺序
#             s[i] = s[j]#最大项赋值给i
#             #此时s[i]的值是最大的，
#             i,j = j,2*j+1#如果父节点不是最大的，调整顺序，则将i,j更新为最大节点和该节点的左子节点，继续进行最大堆构建
#         s[i] = father #如果i是最大的，break到这里，i不变，father位置不变，如果i不是最大的，father被下放到子节点中j
#     end = len(s)
#     for i in range(end//2-1,-1,-1):
#
#         zuidadui(s,s[i],i,end)
#     for i in range((end-1),0,-1):    #只需要从尾部到第一个左子节点,最后剩下一个节点的时候不需要在比较了
#         e = s[i]
#         s[i] = s[0]
#         zuidadui(s,e,0,i)
#     return s



def jishu(s,mins,maxs):

    if s ==[]:
        return s
    length = len(s)

    arr_length = maxs-mins+1

    temp = [0]*arr_length
    # # 输入为空，就返回空列表
    # if collection == []:
    #     return []
    #
    #
    # coll_len = len(collection)
    # coll_max = max(collection)#返回最大值
    # coll_min = min(collection)#返回最小值
    #
    # #计算待排序列表的元素数值区域长度，如4-9共9+1-4=6个数
    # counting_arr_length = coll_max + 1 - coll_min
    # counting_arr = [0] * counting_arr_length  #构造一个全为0列表
    #
    #
    # for number in collection:
    #     counting_arr[number - coll_min] += 1  #统计列表中每个值出现的次数，
    #
    #
    # #使counting_arr[i]存放<=i的元素个数，就是待排序列表中比某个值小的元素有多少个
    # for i in range(1, counting_arr_length):
    #     counting_arr[i] = counting_arr[i] + counting_arr[i-1]
    #
    #
    # ordered = [0] * coll_len   #存放排序结果
    #
    #
    # #使每个元素被放在ordered中正确的位置，升序
    # for i in reversed(range(0, coll_len)): #reversed表示从下标最大的位置到0，为了使排序稳定
    #     ordered[counting_arr[collection[i] - coll_min]-1] = collection[i]#-1是因为下标从0开始的
    #     counting_arr[collection[i] - coll_min] -= 1 #每归位一个元素，就少一个元素
    #
    # return ordered


if __name__ == "__main__":
    s = [5,3,2,8,6,9,1,7,4]
    # a = maopao(s)
    # a = xuanze(s)
    # a = charu(s)
    # a = xier(s)
    # a = guibing(s)
    # a = quick_sort(s)
    # a = dui(s)
    mins = min(s)
    maxs = max(s)
    a = jishu(s,mins,maxs)
    print(a)


