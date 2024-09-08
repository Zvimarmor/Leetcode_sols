# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        answer=[]
        vals = []
        length = 0
        while head:
            length += 1
            vals.append(head.val)
            head = head.next
        
        if length == 0:
            for i in range(k):
                answer.append(None)
            return answer

        array_length = length // k
        array_spare = length % k
        left_k = k

        if array_length == 0:
            for i in range(length):
                blah = ListNode(val= vals[i])
                answer.append(blah)
                left_k -= 1
            for i in range(left_k):
                answer.append(None)
            return answer

        index = 0
        while left_k > 0:
            head = ListNode()
            prev = head
            for j in range(array_length):
                node = ListNode(val= vals[index])
                prev.next = node
                index += 1
                prev = prev.next
            if array_spare != 0:
                node= ListNode(val = vals[index])
                prev.next = node
                index += 1
                array_spare -= 1
                prev = prev.next
            answer.append(head.next)
            left_k -= 1

        return answer


        