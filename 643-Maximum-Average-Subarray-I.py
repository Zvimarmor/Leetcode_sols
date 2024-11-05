class Solution(object):
    def findMaxAverage(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: float
        \\\
        length = len(nums)

        current_sum = sum(nums[:k])
        answer = current_sum

        for i in range(k, length):
            current_sum = current_sum - nums[i - k] + nums[i]  
            answer = max(answer, current_sum) 
        
        return answer / float(k)
