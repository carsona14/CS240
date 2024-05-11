# Carson Adams 
# 4/14/2024
# CS240
# Algorithms HW 2 : Insertion & Selection Sort
# This programs uses an insertion sort algorithm that works over an array 

# pseudo code from Grokking page 35 selection sort algorithm 
# def selectionSort(arr): Sorts an array
# newArr = []
# for i in range(len(arr)):
# smallest = findSmallest(arr)
# newArr.append(arr.pop(smallest))
# return newArr
# print selectionSort([5, 3, 6, 2, 10])

# selection sort algorithm that finds the smallest value 
# sorts from smallest to biggest
def find_smallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):  # Sorts an array using selection sort
    new_arr = []
    while arr:  # While there are elements in the array
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest)) # pop removes and returns the last element
    return new_arr

arr = [5, 3, 6, 2, 10]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)

# pseudo code insertion sort algorithm
# def insertion_sort(arr)
# i in range(length)
# store arr(i) in a key
# find the index of the last value
# while the last position is greater than 0 
# and arrays index is greater than the key
# insert the element in the previous index

# insertion sort algorithm that finds the smallest value 
# sorts from smallest to biggest
def insertion_sort(arr):  # Sorts an array using insertion sort
    for i in range(1, len(arr)):  # Start from second element
        key = arr[i]  # Store the current element to be inserted
        j = i - 1  # Index of the previous element

        # Move elements greater than key to an extra position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Inserts the key 

arr = [5, 3, 6, 2, 10]
insertion_sort(arr)
print("Sorted array is:", arr)

# How do the best, average and worst case time complexities 
# compare between these two algorithms? 
# Why is the best case different between insertion and selection?
# Insertion sorts worst and average time complexity is O(n^2)
# Its best is O(n)
# Selection sorts worst, average, and best time complexity is O(n^2)
# The best case is different for insertion sort because if its already sorted
# it doesnt take up as much time. No elements need to be moved like in selection sort, just added.

# Using numbers-1.txt with both algorithms
# let the user choose what number they want to find
position_value = int(input("What position would you like to find? "))
# r is read mode closes the file properly
with open("numbers-1.txt", "r") as file:
    # readlines and not read so it reads line by line
    # Converts the array to the length as an int
    # First number in the array is position 0
    numbers_array = [int(line) for line in file.read().splitlines()] 
    
    # Make copies for sorting so the selection sort doesnt start with the stuff from insertion sort
    insertion_sorted = numbers_array.copy()
    selection_sorted = numbers_array.copy()

    # Sort arrays
    insertion_sort(insertion_sorted)
    selection_sorted = selection_sort(selection_sorted)

    print("The value in position", position_value, "using insertion sort is", insertion_sorted[position_value])
    print("The value in position", position_value, "using selection sort is", selection_sorted[position_value])

