class Solution(object):
    def countBits(self, n):
        \\\
        :type n: int
        :rtype: List[int]
        \\\
        answer = []

        for i in range(n+1):
            binary = bin(i)[2:]
            number = binary.count('1')
            answer.append(number)

        return answer
        
        