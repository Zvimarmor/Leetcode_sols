class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        answer = []
        maximum = max(candies)
        length = len(candies)
        for i in range(length):
            if candies[i] + extraCandies >= maximum:
                answer.append(True)
            else:
                answer.append(False)

        return answer
        