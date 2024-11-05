class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)

        if len1 > len2:
            len_long = len1
            len_short = len2
            long = str1
            short = str2
        else:
            len_long = len2
            len_short = len1
            long = str2
            short = str1

        divider = ''
        answer = ''

        for i in range(len_short):
            divider += short[i]
            if long.replace(divider,'') == '' and short.replace(divider,'') == '':
                answer = divider

        return answer
