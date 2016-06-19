class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n, i = len(nums), 0
        while i < n:
            if nums[i] == val:
                del nums[i]
                n -= 1
            else:
                i += 1
        return n
