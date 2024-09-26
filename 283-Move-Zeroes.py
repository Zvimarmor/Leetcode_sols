class Solution(object):
    def moveZeroes(self, nums):
        \\\
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        \\\
        length = len(nums)
        non_zero_idx = 0

        for i in range(length):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1


        for i in range(non_zero_idx,length):
            nums[i] = 0
            

        
            

        