# Carson Adams 
# 4/21/2024
# CS240
# Algorithms HW 3 : Recursion vs Iteration
# This programs uses linear and binary search algorithms both recursively and iteratively in pseudo code
# and python code

# Write a linear search algorithm both recursively and iteratively in pseudo code. Comment to explain.

# Iterative Linear Search
# function linearSearch1(arr, target):
#    for each element in arr:
#       if element equals target:
#           return index of element
#   return -1 // if target not found

# Iterates through each element 
# Checks if current element matches target
# If it is target it returns the index of the element.
# Returns -1 if not found

# Recursive linear search
# function linearSearch2(arr, target, index):
#    if index >= length of arr:
#        return -1 // Base case: target not found
#    else if arr[index] equals target:
#        return index // Base case: target found
#    else:
#        return linearSearchRecursive(arr, target, index + 1) // Recursive call 

# Takes the array, target element, and current index as parameters.
# Base case 1: If target not found, return -1.
# Base case 2: If the element at the current index matches the target, return the index.
# Recursive case: If the target is not found, make a recursive call with the next index.

def linear_search_iterative(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1  # Base case target is not found
    elif arr[index] == target:
        return index  # Base case target is found
    else:
        return linear_search_recursive(arr, target, index + 1)
    
# Rewrite the binary search algorithm from week 1 in a recursive form in pseudo code 
# and in the programming language of your choice

# I made it in Java attatched 

# Find a for loop you wrote in previous course work and rewrite it as a recursive function
# (it can not be a simple linear search problem). Please show the original code in your submission.

# I made it in Java attatched

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
values_to_search = [8128705, 5842193]

# binary search for each value
for value in values_to_search:
    position = recursive_binary_search(insertion_sorted, value)
    if position != -1:
        print("The position of",value, "is", position)
    else:
        print(value, "is not found in the list.")
