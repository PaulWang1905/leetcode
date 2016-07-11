class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a, b = len(nums1), len(nums2)
        if a > b:
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1
        n, rst = max(a, b), []
        hashDict = {}
        for i in range(n):
            if long[i] not in hashDict.keys():
                hashDict[long[i]] = 1
            else:
                hashDict[long[i]] += 1
        m = min(a, b)
        for i in range(m):
            if short[i] in hashDict.keys() and hashDict[short[i]] != 0:
                rst.append(short[i])
                hashDict[short[i]] -= 1
        return rst
