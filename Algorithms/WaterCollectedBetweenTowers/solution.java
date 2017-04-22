import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        // Scanner
        Scanner sc = new Scanner(System.in);
        // Input Cases
        int cases = Integer.parseInt(sc.nextLine());
        // Processing each case
        for(int i = 0; i < cases; i++) {
            String[] heights = sc.nextLine().split(" ");
            // Printing the answer from "answer" function in right format.
            System.out.println("Case #" + i+1 + ": " + answer(mapToInt(heights)));
        }
    }

    private static int answer(int[] heights) {
        // Initialize to 0
        int totalWater = 0;
        // For each tower in the array
        for(int i = 0; i < heights.length; i++) {
            // Find heighest tower on left side including itself.
            int leftHigh = findMax(heights, 0, i);
            // Find heighest tower on right side including itself.
            int rightHigh = findMax(heights, i, heights.length - 1);
            /*
             * Water collected over current tower will be height of the lower tower out of
             * left and right heighest towers minus height of the tower itself.
             */
            totalWater += (leftHigh > rightHigh ? rightHigh : leftHigh) - heights[i];
        }
        return totalWater;
    }

    /*
     * Maps an array of Strings to an array of Integers.
     */
    private static int[] mapToInt(String[] arr) {
        int[] returnArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            returnArr[i] = Integer.parseInt(arr[i]);
        }
        return returnArr;
    }

    /*
     * Finds max number out of an array between given starting and ending indices.
     */
    private static int findMax(int[] heights, int start, int end) {
        int currentMax = 0;
        for(int i = start; i <= end; i++) {
            if(heights[i] > currentMax) {
                currentMax = heights[i];
            }
        }
        return currentMax;
    }
}
