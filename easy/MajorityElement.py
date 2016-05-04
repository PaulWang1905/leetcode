class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = len(nums) / 2
        for num in set(nums):
            if nums.count(num) > cnt:
                return num
