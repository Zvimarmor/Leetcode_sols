class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        minimal = len1
        if len1 > len2:
            minimal = len2
            bigger = word1
        elif len2 > len1:
            minimal = len1
            bigger = word2
        else:
            bigger = ''
        answer = ''

        for i in range(minimal):
            answer += word1[i]
            answer += word2[i]

        for i in range(minimal,len(bigger)):
            answer += bigger[i]

        return answer

        