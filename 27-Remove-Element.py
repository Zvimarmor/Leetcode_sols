class Solution(object):
    def removeElement(self, nums, val):
        \\\
        :type nums: List[int]
        :type val: int
        :rtype: int
        \\\
        length = len(nums)
        count = 0
        i=0

        if length == 0:
            return 0

        while i<length:
            if nums[i] == val:
                for j in range(i,length-1):
                    nums[j] = nums[j+1]
                nums.pop()
                length -= 1
            else:
                count += 1
                i+=1
        
        return count
    

        