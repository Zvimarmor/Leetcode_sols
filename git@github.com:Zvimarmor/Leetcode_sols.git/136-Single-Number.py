class Solution(object):
    def singleNumber(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        answer = 0
        length = len(nums)
        
        for i in range(length):
            answer ^= nums[i]

        return answer
        