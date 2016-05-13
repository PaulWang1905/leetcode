class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return nums
        
        rst, i = [], 0
        while i < len(nums) - 1:
            left = i
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if left < i:
                rst.append(repr(nums[left]) + '->' + repr(nums[i]))
                i += 1
            else:
                rst.append(repr(nums[i]))
                i += 1
        if i == len(nums) - 1:
            rst.append(repr(nums[-1]))
        return rst
