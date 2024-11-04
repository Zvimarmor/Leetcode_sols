class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ''
        length = len(s)

        for i in range(length):
            if s[i] == '*':
                answer = answer[:-1]
                i += 1
            else:
                answer += s[i]
                i+= 1

        return answer

        