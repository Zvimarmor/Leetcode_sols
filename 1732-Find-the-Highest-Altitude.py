class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        length = len(gain)
        for i in range(1,length):
            gain[i] = gain[i-1] + gain[i]
        gain.append(0)

        return max(gain)
        