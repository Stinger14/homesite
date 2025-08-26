"""
Hints:
1. nums: list[int], val: int
2. Remove all instances of val in nums in-place.
3. The order of elements can be changed.
4. Return the number of elements left (k) in nums which are not equal to val.
"""

class Solution(object):
    """Given an integer array nums and an integer val, remove all occurrences of val 
        in nums in-place. The order of the elements may be changed. Then return the number 
        of elements in nums which are not equal to val.
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [num for num in nums if num != val]
        k = len(nums)
        return k
        # k = 0
        # tmp_nums = nums[:]
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         tmp_nums.remove(val)
        #         k += 1
        # nums = tmp_nums[:]
        # return k, nums

print(Solution().removeElement([3, 2, 2, 3], 3))
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
