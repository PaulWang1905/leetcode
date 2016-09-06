'''
method: use the index of list
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                if nums[i]*2 == target:
                    if nums.count(nums[i]) > 1:
                        return i+1, i+2+nums[i+1:].index(nums[i])
                        break
                    else:
                        continue
                else:
                    return i+1, nums.index(target-nums[i])+1
                    break
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                try:
                    return [i, nums.index(target-nums[i], i+1)]
                except ValueError:
                    continue
