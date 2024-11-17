# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length = 0
        answer = ListNode(next = head)
        node = ListNode(next = head)
        curr = ListNode(next = head)

        while curr.next:
            length += 1
            curr = curr.next

        if length == 1:
            return
        
        length = length / 2
        prev = node
        node = node.next

        while length > 0:
            prev = prev.next
            node = node.next
            length -= 1

        prev.next = node.next

        return answer.next

        


        


        