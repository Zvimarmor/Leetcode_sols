class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0
        while a > 0 or b > 0 or c > 0:
            # Get the least significant bits (LSBs) of a, b, and c
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            # Case 1: c's bit is 1
            if bit_c == 1:
                # At least one of a or b must have a 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            
            # Case 2: c's bit is 0
            else:
                # Both a and b must have 0
                if bit_a == 1:
                    flips += 1
                if bit_b == 1:
                    flips += 1
            
            # Right shift a, b, and c to process the next bit
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
        