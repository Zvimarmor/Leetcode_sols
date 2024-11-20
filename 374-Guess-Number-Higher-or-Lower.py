# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        \\\
        :type n: int
        :rtype: int
        \\\

        start, end = 1,n

        while start <= end:
            mid = start + (end-start) //2
            answer = guess(mid)

            if answer == 0:
                return mid

            elif answer == -1:
                end = mid-1

            elif answer == 1:
                start = mid+1

            

            



        