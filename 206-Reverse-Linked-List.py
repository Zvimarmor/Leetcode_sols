# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        values = []
        length = 0

        if not head:
            return
        
        while head:
            values.append(head.val)
            head = head.next
            length += 1

        curr = ListNode()
        prev = ListNode(next = curr)
        answer = prev

        for i in range(length):
            curr = ListNode(val = values[length-i-1])
            prev.next = curr
            prev = prev.next

        return answer.next


        