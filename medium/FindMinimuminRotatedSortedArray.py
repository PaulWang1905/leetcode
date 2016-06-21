class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #if n == 1:
        #    return nums[0]
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]
