class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time_diff = []
        length = len(timePoints)
        for i in range(length):
            for j in range(length):
                if i == j :
                    continue
                time1 = timePoints[i]
                time2 = timePoints[j]
                if time1 == time2:
                    return 0
                diff = abs((60*int(time1[0:2])+int(time1[3:5]))-(60*int(time2[0:2])+int(time2[3:5])))
                time_diff.append(min(diff, 24*60-diff))

        return min(time_diff)
        