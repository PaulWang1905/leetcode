class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        nums.sort()
        middle = len(nums) / 2
        return min(sum(map(lambda x: abs(x-nums[middle]), nums)), sum(map(lambda x: abs(x-nums[middle-1]), nums)))
