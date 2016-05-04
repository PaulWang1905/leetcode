class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
            
        left = right = nums.index(target)
        while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
        return [left, right]
