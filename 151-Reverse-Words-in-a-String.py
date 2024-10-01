class Solution(object):
    def reverseWords(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        words = s.split(' ')
        answer = ''
        length = len(words)
        for i in range(length):
            word = words[length-i-1]
            if word:
                answer += word
                answer += ' '

        answer = answer[:-1]

        return answer
        