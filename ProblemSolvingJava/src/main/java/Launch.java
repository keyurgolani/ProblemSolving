import java.util.List;
import java.util.Scanner;

/**
 * Created by keyurgolani on 5/31/17.
 */
public class Launch {
    public static void main(String...args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number count.");
        int length = sc.nextInt();
        System.out.println("Enter Numbers.");
        int[] values = new int[length];
        for (int i = 0; i < length; i++) {
            values[i] = sc.nextInt();
        }
        System.out.println(Module1.sumOfInts(values));
    }
}
