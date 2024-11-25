class Solution(object):
    def compress(self, chars):
        \\\
        :type chars: List[str]
        :rtype: int
        \\\
        length = len(chars)
        s = []

        if length == 1:
            return 1

        curr = chars[0]
        count = 1
        for i in range(1, length):
            if chars[i] == curr:
                count += 1

            elif chars[i] != curr and count == 1:
                s.append(curr)
                curr = chars[i]

            elif chars[i] != curr and count != 1:
                s.append(curr)
                if count < 10:
                    s.append(str(count))
                else:
                    strlen = len(str(count))
                    for j in range(strlen):
                        s.append(str(count)[j])
                curr = chars[i]
                count = 1

        s.append(curr)
        if count != 1:
            if count < 10:
                    s.append(str(count))
            else:
                strlen = len(str(count))
                for j in range(strlen):
                    s.append(str(count)[j])

        chars[:] = s
        return len(s)




        




        
        