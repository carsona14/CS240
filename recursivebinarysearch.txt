# Use the following attached documents to test your search algorithms
# numbers-3.txt Download numbers-3.txt Use one of your sorting algorithms 
# to sort the list first before implementing binary search. 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def recursive_binary_search(arr, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

# Load the numbers from the file
with open("numbers-3.txt", "r") as file:
    numbers_array = [int(line) for line in file.read().splitlines()]

# Make a copy for sorting
insertion_sorted = numbers_array.copy()

# Insertion sort
insertion_sort(insertion_sorted)

# Values to search for
target_numbers= [8128705, 5842193]

# binary search for each value
for value in target_numbers:
    position = recursive_binary_search(insertion_sorted, value)
    if position != -1:
        print("The position of",value, "is", position)
    else:
        print(value, "is not found in the list.")