public class BinarySearch {
        public static void main(String[] args) {
        int[] numbersArray = {1, 3, 5, 7, 9, 11, 13, 15, 17, 21};
        int numberNeeded = 11;

        int[] result = binarySearch(numbersArray, numberNeeded);

        if (result[0] != -1) {
            System.out.println("Number found at index " + result[0] + " with " + result[1] + " operations.");
        } else {
            System.out.println("Number not found with " + result[1] + " operations.");
        }
    }
    public static int[] binarySearch(int[] numbersArray, int numberNeeded) {
        int beginning = 0;
        int operationCount = 0;
        int end = numbersArray.length - 1;
        int[] result = new int[2];

        while (beginning <= end) {
            operationCount++;
            int mid = (beginning + end) / 2;

            if (numbersArray[mid] == numberNeeded) {
                result[0] = mid;
                result[1] = operationCount;
                return result;
            } else if (numbersArray[mid] < numberNeeded) {
                beginning = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        result[0] = -1;
        result[1] = operationCount;
        return result;
    }
}

// Find a for loop you wrote in previous course work and rewrite it as a recursive function
// (it can not be a simple linear search problem). Please show the original code in your submission.