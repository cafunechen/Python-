# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:

    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        if head1.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == head1.val and head1.next is not None:
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication(head1)
            else:
                return None
        return pHead
    # def deleteDuplication(self, pHead):
    #     # write code here
    #     res = []
    #     while pHead:
    #         res.append(pHead.val)
    #         pHead = pHead.next
    #     res = list(filter(lambda x: res.count(x)==1,res))
    #     newList = ListNode(0)
    #     pre = newList
    #     for i in res:
    #         node = ListNode(i)
    #         pre.next = node
    #         pre = pre.next
    #     return newList.next

if __name__ =="__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(3)
    a5 = ListNode(4)
    a6 = ListNode(4)
    a7 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7
    a = Solution()
    x = a.deleteDuplication(a1)
    for i in range(3):
        print(x.val)
        x = x.next
