"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

print(canJump([2,3,1,1,4]))  # True
print(canJump([3,2,1,0,4]))  # False
print(canJump([0]))  # True
print(canJump([2,0]))  # True
print(canJump([2,0,0]) ) # True
# canJump([1,1,1,0])  # True
# canJump([1,1,1,1])  # True
# canJump([1,1,1,1,0])  # True
# canJump([1,1,1,1,1])  # True
canJump([1,2,0,1,1,0])


