class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = len(s)
        count = 0
        answer = 0

        if length == 1:
            if s[0] in ['a','e','i','o','u']:
                return 1
            return 0
        
        for i in range(k):
            if s[i] in ['a','e','i','o','u']:
                count += 1
        answer = count 

        # Sliding window logic
        for i in range(k, length):
            if s[i - k] in ['a','e','i','o','u']:
                count -= 1
            if s[i] in ['a','e','i','o','u']:
                count += 1
            answer = max(answer, count)

        return answer