class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer1 = []
        len1 = len(nums1)
        answer2 = []
        len2 = len(nums2)

        for i in range(len1):
            if nums1[i] not in nums2:
                if not nums1[i] in answer1:
                    answer1.append(nums1[i])
        
        for i in range(len2):
            if nums2[i] not in nums1:
                if not nums2[i] in answer2:
                    answer2.append(nums2[i])

        return [answer1,answer2]

        