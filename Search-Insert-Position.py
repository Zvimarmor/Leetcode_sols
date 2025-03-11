class Solution(object):
    def searchInsert(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: int
        \\\
        start, end = 0, len(nums)

        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return start
