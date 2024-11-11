class Solution(object):
    def increasingTriplet(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        min = 99999999999
        max = 99999999999 
        
        for num in nums:
            if num <= min:
                min = num 
            elif num <= max:
                max = num  
            else:
                return True
                
        return False
