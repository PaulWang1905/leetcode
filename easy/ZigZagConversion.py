'''
two-dimension list
'''

class Solution(object):
	def convert(self, s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	if numRows == 1:
		return s
	period = 2 * (numRows - 1)
	rst = [''] * numRows
	for i in range(len(s)):
		tmp = i % period
		if tmp < numRows:
			rst[tmp] += s[i]
		else:
			rst[2*numRows-tmp-2] += s[i]
	return ''.join(rst)
