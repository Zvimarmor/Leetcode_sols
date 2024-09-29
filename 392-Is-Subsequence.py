class Solution(object):
    def isSubsequence(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: bool
        \\\
        lens = len(s)
        lent = len(t)
        for i in range(lens):
            idx = t.find(s[i])
            if idx == -1:
                return False
            t = t[idx+1:]
            print(t)
        return True

        
        