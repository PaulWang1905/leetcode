class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst, result = [], 1
        n, cnt = len(nums), nums.count(0)
        if cnt > 1:
            return [0] * n
        if cnt == 1:
            j = 0
            for i in range(n):
                if nums[i] != 0:
                    rst.append(0)
                    result *= nums[i]
                else:
                    j = i
            rst.insert(j, result)
            return rst
        else:
            for i in range(n):
                result *= nums[i]
            for i in range(n):
                rst.append(result / nums[i])
            return rst
