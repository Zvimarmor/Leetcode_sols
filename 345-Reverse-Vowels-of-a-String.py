class Solution(object):
    def reverseVowels(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        length = len(s)
        to_reverse = []
        len2 = 0
        for i in range(length):
            if s[i] in ['I','E','A','O','U','i','e','a','o','u']:
                to_reverse.append(i)
                len2 += 1

        s = list(s)

        for i in range(len2//2):
            curr = s[to_reverse[i]]
            s[to_reverse[i]] = s[to_reverse[len2-1-i]]
            s[to_reverse[len2-1-i]] = curr
        return ''.join(s)

        

        