'''
decide whether the difference between index and value is equal or not
'''

class Solution(object):
	def longestConsecutive(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums = list(set(nums))
	nums.sort()
	cnt = rst = 1
	for i in range(len(nums)-1):
		if nums[i] - i == nums[i+1] - i - 1:
			cnt += 1
		else:
			cnt = 1
		rst = max(rst, cnt)
	return rst
