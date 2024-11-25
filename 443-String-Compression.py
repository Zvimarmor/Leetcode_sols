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
            print(curr,count)
            if chars[i] == curr:
                count += 1

            elif chars[i] != curr and count == 1:
                s.append(curr)
                curr = chars[i]

            elif chars[i] != curr and count != 1:
                s.append(curr)
                for j in range(len(str(count))):
                    s.append(str(count)[j])
                curr = chars[i]
                count = 1

        s.append(curr)
        if count != 1:
            for i in range(len(str(count))):
                    s.append(str(count)[i])

        chars[:] = s
        return len(s)




        




        
        