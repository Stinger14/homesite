"""
Write a Python function that takes a list of integers as input 
and returns the sum of all even numbers in the list.
"""

def sum_even_numbers(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum


input_list = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(input_list))  # Output should be 12 (2 + 4 + 6)
