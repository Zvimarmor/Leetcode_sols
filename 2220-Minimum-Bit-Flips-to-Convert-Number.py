class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        answer = 0
        
        # while start != 0 or goal != 0:
        for i in range(30):
            check_start = True
            check_end = True
            if (start-(2**(29-i))) >= 0:
                check_start = True
                start -= (2**(29-i))
            else:
                check_start = False

            if (goal-(2**(29-i))) >= 0:
                check_end = True
                goal -= (2**(29-i))
            else:
                check_end = False

            if check_start != check_end:
                answer += 1

        return answer

            
            