# Carson Adams 
# 4/7/2024
# CS240
# Algorithms HW 1 : Binary Search, Time Complexity
# This programs puts a txt file into an array then uses a binary search algorithm iteratively to 
# give the position and amount of operations taken to find that position

#pseudo code
# open txt file
# def BinarySearch(array, position)
# left of middle, right of middle
# while left <= right
# keep dividing one side by 2
# report position based on number of divisions 
# report number of divisions

# let the user choose what number they want to find
number_needed = int(input("What number would you like to find? "))
# r is read mode closes the file properly
with open("numbers.txt", "r") as file:
    # readlines and not read so it reads line by line
    # Converts the array to the length as an int
    # First number in the array is position 0
    numbers_array = [int(line) for line in file.read().splitlines()]
    # layout inspired by Grokking binary search
    def BinarySearch(numbers_array, number_needed):
        beginning = 0
        operation_count = 0
        end = len(numbers_array) - 1

        while beginning <= end:
            operation_count += 1
            mid = (beginning + end) // 2

            if numbers_array[mid] == number_needed:
                return mid, operation_count
            elif numbers_array[mid] < number_needed:
                beginning = mid + 1
            else:
                end = mid - 1
        return -1, operation_count
    
    # returns position of number_needed within the numbers_array 
    number_position, operation_count = BinarySearch(numbers_array, number_needed)
    print("The position of", number_needed, "is", number_position)
    print("It took",operation_count, "operations to find",number_needed)

    # The worst time complexity is O(Log n) from the binary search,
    # The time complexity would be the same if it was 4000 elements because n represents a variable
    # The average time complexity for binary search is O(Log n) because it halves a halve ect.

    #   function sum(arr){
    #counter = 0 O(1)

    #for (i = 0; i < arr.length; i++) { O(n)
    #    counter += arr[i] 
    #}

    #    return counter O(1)
    #}
    # Overall: O(n)

    #b. 
    #function getXOR(arr1, arr2){

    #arr3 = [] O(1)

    #for (i = 0; i < arr1.length; i++){
    #    let unique = True O(1)
    #    for (j = 0; j < arr2.length; j++ }{ O(n)
    #        if(arr1[i] == arr2[j]) {unique = False;} O(1)
    #    }
    #    if (unique) {arr3.append(arr1[i]);} O(1)
    #    }
    #}  
    #for (i = 0; i < arr2.length; i++){ O(n)
    #    for (j = 0; j < arr1.length; j++ }{ O(n)
    #    if(arr2[i] == arr1[j]) {unique = False;} O(1)
    #    }
    #    if (unique) {arr3.append(arr2[i]);} O(1)
    #}
    #return arr[3] O(1)
    #}    
    # Overall: O(n^2)
