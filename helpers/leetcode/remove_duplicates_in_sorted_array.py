from time import process_time as time

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        k = 1
        for i in nums:
            if nums.count(i) > 1:
                nums.remove(i)
                k += 1
        return k

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

start_time = time()
print(Solution2().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
end_time = time()
et = (end_time - start_time) * 1000
print(f"Execution time: {et:.8f} ms")