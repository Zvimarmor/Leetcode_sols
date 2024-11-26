class Solution(object):
    def maxArea(self, height):
        \\\
        :type height: List[int]
        :rtype: int
        \\\
        length = len(height)

        if length == 2:
            return min(height[0],height[1])

        start = 0 
        end = length-1
        answer = min(height[start],height[end])*(end-start)

        while start < end:
            cal = min(height[start],height[end])*(end-start)
            if cal > answer:
                answer = cal
            if height[start] <= height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1

        return answer

