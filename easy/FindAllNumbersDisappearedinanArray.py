ass Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = set(range(1, len(nums) + 1))
        return sorted(list(tmp.difference(set(nums))))
