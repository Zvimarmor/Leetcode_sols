# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        \\\
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        \\\
        l1_num = 0
        l2_num = 0
        counter = 0
        curr = l1
        while curr:
            l1_num += curr.val * 10**counter
            counter+=1
            curr = curr.next
        counter = 0
        curr = l2
        while curr:
            l2_num += curr.val * 10**counter
            counter+=1
            curr = curr.next

        answer = l1_num+l2_num
        length = len(str(answer))

        curr = ListNode(val = int(str(answer)[length-1]))
        answer_ = ListNode(next = curr)
        prev = answer_
        for i in range(length):
            curr = ListNode(val = int(str(answer)[length-i-1]))
            prev.next = curr
            prev = prev.next

        return answer_.next



        