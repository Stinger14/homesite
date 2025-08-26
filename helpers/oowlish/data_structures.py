"""
Implement a function to find the k-th largest element in an unsorted list of integers.
"""

def find_kth_largest(input_list, k):
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list[k - 1]


input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
k = 3

print(find_kth_largest(input_list, k))  # Should return 5
