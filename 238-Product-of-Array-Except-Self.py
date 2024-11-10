class Solution(object):
    def productExceptSelf(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[int]
        \\\
        length = len(nums)
        answer = []
        
        mult = 1
        is_zero = False
        zero_num = 0

        for i in range(length):
            if nums[i] == 0:
                is_zero = True
                zero_num += 1
            else:
                mult *= nums[i]

        if is_zero:
            if zero_num == length:
                return [0 for i in range(length)]
                
            for i in range(length):
                if nums[i] == 0:
                    if zero_num >= 2:
                        answer.append(0)
                    else:
                        answer.append(mult)
                else:
                    answer.append(0)
            return answer

        for i in range(length):
            answer.append(mult/nums[i])

        return answer

        