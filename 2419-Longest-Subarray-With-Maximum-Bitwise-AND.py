class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        length = len(nums)
        answer = 0
        current = 0
        for i in range(length):
            if nums[i] == max_val:
                current+=1
            else:
                if current>answer:
                    answer = current
                current = 0

        if current > answer:
            return current

        return answer

        