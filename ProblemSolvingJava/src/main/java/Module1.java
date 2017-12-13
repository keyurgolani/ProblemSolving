import Utils.Node;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by keyurgolani on 5/31/17.
 */
public class Module1 {
    public static int sumOfInts(int...values) {
        int answer = 0;
        for(int value: values) {
            answer += value;
        }
        return answer;
    }

    public HashMap<Node, Integer> verticleSumOfBinaryTree(Node head) {
        Queue<Node> container = new LinkedList<Node>();
        container.add(head);
        int verticleLine = 0;
        while(container.peek() != null) {

        }
        return null;
    }

}
