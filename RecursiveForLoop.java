// Original 

// for (int i = 0; i < rows; i++) {
//     for (int j = 0; j < cols; j++) {
//         if (asterisks[i][j]) {
//             System.out.print("* ");
//         } else {
//             System.out.print("o ");
//         }
//     }
//     System.out.println();
// }

// Recursive

// if (row < rows) {
//     if (col < cols) {  // Base Case
//         if (asterisks[row][col]) {
//             System.out.print("* ");
//         } else {
//             System.out.print("o ");
//         }
//         printAsterisks(asterisks, row, col + 1, rows, cols); // Recursive call
//     } else {
//         System.out.println(); // Recursive call
//         printAsterisks(asterisks, row + 1, 0, rows, cols);
//     }
// }