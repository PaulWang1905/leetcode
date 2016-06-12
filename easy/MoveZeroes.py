class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1
