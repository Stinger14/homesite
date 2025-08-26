"""
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
"""

# nums = [2,3,1,1,4]

def min_jumps(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps

print(min_jumps([2,3,1,1,4])) # 2

# def jump(nums: list[int]) -> int:
#     max_jump = 0
#     steps = 0
#     for i, j in enumerate(nums):
#         if i > max_jump:
            
#         if j <= max_jump and i + j < len(nums):
#             max_jump = nums[i]
#             steps += 1
#     return steps

# print(jump([2,3,1,1,4])) # 2
