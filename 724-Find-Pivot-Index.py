class Solution(object):
    def pivotIndex(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        length = len(nums)
        if length == 1:
            return 0
        
        for i in range(length):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1
        