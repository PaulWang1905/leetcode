class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myNums = list(set(nums))
        if len(myNums) < 3:
            return max(nums)
        return sorted(myNums)[-3]
