"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?


Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""

from heapq import heappush, heappop

def largest_number(nums, k):
    heap = []
    for value in nums:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(nums))]

print(largest_number([3,2,1,5,6,4], 2))
