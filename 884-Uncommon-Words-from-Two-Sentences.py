class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        word_dict = dict()
        s1words = s1.split()
        s2words = s2.split()

        for word in s1words+s2words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        return [word for word in word_dict if word_dict[word] == 1]
        