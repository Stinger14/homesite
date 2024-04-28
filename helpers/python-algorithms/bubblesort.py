  
def bubbleSort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Swap if the element found is greater than the next element
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
