class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        \\\
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        \\\
        length = len(flowerbed)
        i = 0
        
        if n == 0:
            return True

        elif length == 1 and flowerbed[0] == 0:
            return n <= 1
        elif flowerbed[0] == 1:
            i += 1
        elif length > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n-=1

        while i < length-1:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                n-=1
                flowerbed[i] = 1
            i+=1

        if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
            n-=1
        elif flowerbed[length-1] == 1 and flowerbed[length-2] == 1:
            n+=1

        if n >0:
            return False
        return True

        