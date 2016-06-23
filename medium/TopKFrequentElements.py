class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in c[:k]]
