# Pesudo Code:
# def quicksort(array):
# if len(array) < 2:
# return array Base case: arrays with 0 or 1 element are already “sorted.”
# else:
# pivot = array[0] Recursive case
# less = [i for i in array[1:] if i <= pivot] 
# greater = [i for i in array[1:] if i > pivot] Sub-array of all the elements
# greater than the pivot
# return quicksort(less) + [pivot] + quicksort(greater)
# print quicksort([10, 5, 2, 3])

# How do the best, average and worst case time complexities compare between these two algorithms? 
# Merge sort is all O(n log n) and quicksort is O(n log n) but can be O(n^2) at worst

# Quicksort algorithm modified from Grokking page 65
def quicksort(array):
    # Base case
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
# Finds position of value
def find_position(sorted_array, value):
    if value in sorted_array:
        return sorted_array.index(value) + 1
    else:
        return -1

# Load the numbers from the file
with open('numbers-4.txt', 'r') as file:
    numbers = [int(line) for line in file.read().splitlines()]

    # quicksort numbers from file
    sorted_numbers = quicksort(numbers)

    # Target numbers
    values_to_search = [90262, 11559]

    # Print positions
    for value in values_to_search:
        position = find_position(sorted_numbers, value)
        if position != -1:
            print("The position of", value, "is", position)
        else:
            print(value, "is not found in the list.")