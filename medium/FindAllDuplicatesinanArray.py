class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        numDict, res = Counter(nums), []
        for k,v in numDict.items():
            if v > 1:
                res.append(k)
        return res
