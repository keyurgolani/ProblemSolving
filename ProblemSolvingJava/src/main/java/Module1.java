import org.jetbrains.annotations.Contract;

/**
 * Created by keyurgolani on 5/31/17.
 */
public class Module1 {
    @Contract(pure = true)
    public static int sumOfInts(int...values) {
        int answer = 0;
        for(int value: values) {
            answer += value;
        }
        return answer;
    }
}
