class Solution(object):
    def lengthOfLastWord(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        length = len(s)
        i = length-1
        ans = 0
        if length == 0:
            return 0
        if length == 1:
            if s[0] == ' ':
                return 0
            return 1

        while s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            ans += 1
            i-=1
        return ans

        