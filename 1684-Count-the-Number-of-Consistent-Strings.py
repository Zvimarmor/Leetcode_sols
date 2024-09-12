class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        answer = 0
        allowed = set(allowed)
        for i in range(length):
            word_ind = True
            for char in set(words[i]):
                if char not in allowed:
                    word_ind = False
            if word_ind:
                answer += 1

        return answer

        