"""
This script demonstrates the use of the bisect module to insert items 
into a sorted list.

The script generates a random list of numbers and inserts them into the list 
in sorted order using the bisect.insort() function.

The sorted list is printed after each insertion.

Parameters:
- SIZE: The number of items to generate and insert into the list.

Returns:
None
"""

import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

