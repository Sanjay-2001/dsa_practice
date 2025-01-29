def findSecondLargestAndSmallest(arr):
    if len(arr) < 2:
        return None, None  # Not enough elements

    first_smallest, second_smallest = float('inf'), float('inf')
    first_largest, second_largest = float('-inf'), float('-inf')

    for num in arr:
        # Update smallest values
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            second_smallest = num

        # Update largest values
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num

    return second_smallest, second_largest


arr = [2, 1, 14, 5, 16, 3]
second_smallest, second_largest = findSecondLargestAndSmallest(arr)

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
