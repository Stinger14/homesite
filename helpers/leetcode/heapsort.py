"""
Heapsort example
"""
from heapq import heappush, heappop

def heapsort(nums):
    heap = []
    for value in nums:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(nums))]

# print(largest_number([3,2,1,5,6,4], 2))
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
