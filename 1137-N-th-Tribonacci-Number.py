class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1 or n ==2:
            return 1

        answer_arr = [0,1,1]
        length = 2
        for i in range(n-2):
            answer_arr.append(answer_arr[length-2]+answer_arr[length-1]+answer_arr[length])
            length += 1

        return answer_arr[-1]
        