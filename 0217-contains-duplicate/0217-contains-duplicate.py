class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checking =set()
        for num in nums:
            if num in checking:
                return True
            checking.add(num)
        return False
        