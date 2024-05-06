# MergeSort(array)
#    if length of array <= 1
#        return array
#    else
#        mid = length of array // 2
#        left_half = MergeSort(first half of array)
#        right_half = MergeSort(second half of array)
#        return Merge(left_half, right_half)
# Merge(left, right)
#    result = []
#    left_index = 0
#    right_index = 0
#    
#    while left_index < length of left and right_index < length of right
#        if left[left_index] <= right[right_index]
#            append left[left_index] to result
#            increment left_index
#        else
#            append right[right_index] to result
#            increment right_index
#    
#    append remaining elements of left and right to result
    
#    return result

# Main:
#    Read numbers from the file
#    numbers = parse numbers from file  
#    sorted_numbers = MergeSort(numbers)
#    values_to_search = [90262, 11559]  
#    for each value in values_to_search
#        position = FindPosition(sorted_numbers, value)
#        if position != -1
#            print "The position of", value, "is", position
#        else
#            print value, "is not found in the list."


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left_half = merge_sort(array[:mid])
        right_half = merge_sort(array[mid:])
        return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def find_position(sorted_array, value):
    if value in sorted_array:
        return sorted_array.index(value) + 1
    else:
        return -1

# Read numbers from the file
with open('numbers-4.txt', 'r') as file:
    numbers = [int(line) for line in file.read().splitlines()]

    # Apply merge sort
    sorted_numbers = merge_sort(numbers)

    # Find positions of specific numbers
    values_to_search = [90262, 11559]

    # Print positions
    for value in values_to_search:
        position = find_position(sorted_numbers, value)
        if position != -1:
            print("The position of", value, "is", position)
        else:
            print(value, "is not found in the list.")
