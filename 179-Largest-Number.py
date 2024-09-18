class Solution(object):
    def largestNumber(self, nums):
        \\\
        :type nums: List[int]
        :rtype: str
        \\\
        # Convert all numbers to strings for comparison
        nums_str = list(map(str, nums))
        
        # Custom sorting using bubble sort (or another sorting algorithm)
        for i in range(len(nums_str)):
            for j in range(i + 1, len(nums_str)):
                # Compare based on concatenated values
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    # Swap the numbers if needed
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
        
        # Join the sorted numbers into the answer
        answer = ''.join(nums_str)
        
        # Handle case where the result is '0' (e.g., [0, 0])
        return answer if answer[0] != '0' else '0'