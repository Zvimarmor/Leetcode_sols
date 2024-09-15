class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel_dict = set()
        length = len(s)
        answer = 0

        first_occurrence = {0: -1}  # Initial state where no vowels have been encountered
        bitmask = 0  # Start with an empty bitmask (00000)
        max_len = 0  # Variable to store the maximum length of the substring
        
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                bitmask ^= (1 << vowel_to_bit[char])  # XOR to flip the bit
            
            if bitmask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[bitmask])
            else:
                first_occurrence[bitmask] = i
        
        return max_len