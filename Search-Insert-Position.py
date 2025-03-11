class Solution(object):
    def searchInsert(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: int
        \\\
        length = len(nums)
        def helper(nums,start,end,target):
            i = start + (end - start) // 2
            print(start,end,i)
            if start >= end:
                return start
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return helper(nums,start,i,target)
            elif nums[i] < target:
                return helper(nums,i+1,end,target)

        return helper(nums,0,length,target)
            

        