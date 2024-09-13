class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix_xor = [0] * (len(arr) + 1)
        
        for i in range(1, len(arr) + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        answer = []
        
        for query in queries:
            left, right = query
            answer.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return answer
            
        