# -*- coding:utf-8 -*-
# 二分查找
def binary_chop(alist, data):

    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False

if __name__ == '__main__':
    lis = [2,4, 5, 12, 14, 23]
    if binary_chop(lis, 14):
        print('ok')
