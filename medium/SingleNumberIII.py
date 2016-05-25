class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        rst, cnt, i = [], 0, 1
        if nums[0] != nums[1]:
            rst.append(nums[0])
            cnt += 1
        while i < len(nums) - 1:
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                rst.append(nums[i])
                cnt += 1
                if cnt == 2:
                    return rst
            i += 1
        if cnt == 1:
            rst.append(nums[-1])
            return rst
