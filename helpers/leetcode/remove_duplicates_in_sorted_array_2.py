from time import process_time as time

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an integer array nums sorted in non-decreasing order, 
        remove some duplicates in-place such that each unique element appears at most twice.
        """       
        if len(nums) <= 2:
            return len(nums)

        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i        

start_time = time()
print(Solution().removeDuplicates([1,1,1,2,2,3]))
end_time = time()
et = (end_time - start_time) * 1000
print(f"Execution time: {et:.8f} ms")