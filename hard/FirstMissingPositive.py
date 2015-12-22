'''
method: swap, put a[i] in position a[i]-1
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i]>=len(nums) or nums[i]<=0 or nums[i]==nums[nums[i]-1]:
                    break
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
        j = 0
        for i in range(len(nums)):
            if nums[i] != i+1:
                break
            j += 1
        if j == len(nums):
            return j+1
        else:
            return i+1
