class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2 or k < 0:
            return 0
    
        nums.sort()
        rst = []
        left, right = 0, 1
        while right < len(nums):
            temp = nums[left] + k
            if temp == nums[right]:
                rst.append((nums[left], nums[right]))
                left += 1
                right += 1
            elif temp < nums[right]:
                left += 1
                if left == right:
                    right += 1
            else:
                right += 1
        return len(set(rst))
