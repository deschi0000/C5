import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
public class Main {

    public static void main(String[] args) {
        // NB rows and columns must be equal amounts
        int[][] myArray = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int arrayLength = myArray.length;

        // debugging
        // testCase();
        System.out.printf("=======================================%n");

        System.out.printf("Hello and welcome!");
        System.out.printf("\nHow many times would you like to rotate? 90 / 180 / 270?: ");


        // ask user for how many rotations
        Scanner scanner = new Scanner(System.in);
        int rotations = scanner.nextInt();
        rotations = rotations / 90;
        System.out.print("your choice: " + rotations);


        // print the original matrix, rotate, print new matrix
        System.out.print("\nOriginal Array: \n");
        printMatrix(myArray);

        // initialize the array
        int[][] newMatrix = new int[arrayLength][arrayLength];


        // wrapped in number of times you want to rotate
        for (int i = 0; i < rotations; i++) {
            if (i == 0){
                newMatrix = rotateArray(myArray);
            }
            else {
                newMatrix = rotateArray(newMatrix);
            }
        }
        System.out.print("\nRotated Array: \n");
        printMatrix(newMatrix);
    }

    // method for rotating by 9 degrees
    public static int[][] rotateArray(int[][] myArray){
        // get the length of the sub-arrays
        int subArrayLength = myArray[0].length;
        // initiate a new matrix with the sizes (n*n, though more convoluted this way)
        int[][] newMatrix = new int[myArray.length][subArrayLength];


        int subArrayIndex = 0;  // will only go to the length of the sub-array
        for (int i = 0; i < myArray[0].length; i++) {
            // create a temp sub-array
            int[] tempSubArray = new int[subArrayLength];
            // initiate which index each iteration will place into the temp sub-array
            int newSubArrayIndex = 0;

            // iterate through each sub-array, pulling the appropriate values to the corresponding index
            for (int j = myArray.length-1; j >= 0; j--) {
//                System.out.printf("%d ", myArray[j][subArrayIndex]);  // check the order
                tempSubArray[newSubArrayIndex] = myArray[j][subArrayIndex];
                newSubArrayIndex++;
                newMatrix[i] = tempSubArray;
            }
            subArrayIndex++;
        }
        return newMatrix;
    }
    // method for printing out the matrix
    public static void printMatrix(int[][] myArray){
        for (int i = 0; i < myArray.length; i++) {
            for (int j = 0; j < myArray[i].length; j++) {
                System.out.print(myArray[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void testCase(){
        // test arrays, could add ability to make new arrays?
        int[][] myArray1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] myArray2 = {{0, 1, 2, 3}, {3, 4, 5, 6}, {6, 7, 8, 9},{6, 7, 8, 9}};

        System.out.print("\nOriginal Array: \n\n");
        printMatrix(myArray1);

        int[][] newMatrix = rotateArray(myArray1);

        System.out.print("\nRotated Array: \n\n");
        printMatrix(newMatrix);
    }

}