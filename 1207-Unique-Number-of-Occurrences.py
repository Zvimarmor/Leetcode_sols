class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        length = len(arr)
        ansdict = dict()

        if length == 1:
            return True

        for i in range(length):
            if arr[i] in ansdict.keys():
                ansdict[arr[i]] += 1
            else:
                ansdict[arr[i]] = 1

        numsdict = dict()

        for key in ansdict:
            if ansdict[key] in numsdict.keys():
                numsdict[ansdict[key]].append(key)
            else:
                numsdict[ansdict[key]]= [key]

        for key in numsdict:
            if len(numsdict[key]) >= 2:
                return False

        return True

        