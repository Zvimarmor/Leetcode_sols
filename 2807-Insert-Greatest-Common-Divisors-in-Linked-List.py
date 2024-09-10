# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        answer = head
        prev = head
        head = head.next

        def gcd(x,y):
            while y != 0:
                x, y = y, x % y
            return x

        while head:
            node_val = gcd(prev.val,head.val)
            node = ListNode(val = node_val,next = head)
            prev.next = node
            prev = prev.next.next
            head=head.next

        return answer

        