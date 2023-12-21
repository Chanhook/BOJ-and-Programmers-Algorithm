import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        String[] split = str.split("");

        Stack<Object> stack = new Stack<>();

        int value = getValue(split, stack);
        bw.write(value + "\n");
        bw.flush();
        br.close();
        bw.close();
    }

    private static int getValue(String[] split, Stack<Object> stack) {
        for (String s : split) {
            if (s.equals("(") || s.equals("[")) {
                stack.push(s);
            } else if (s.equals(")")) {
                int temp = 0;
                while (!stack.isEmpty() && !stack.peek().equals("(")) {
                    Object obj = stack.pop();
                    if (obj instanceof String) {
                        return 0;
                    } else {
                        temp += (int) obj;
                    }
                }
                if (stack.isEmpty()) {
                    return 0;
                }
                stack.pop();
                if (temp == 0) {
                    stack.push(2);
                } else {
                    stack.push(2 * temp);
                }
            } else if (s.equals("]")) {
                int temp = 0;
                while (!stack.isEmpty() && !stack.peek().equals("[")) {
                    Object obj = stack.pop();
                    if (obj instanceof String) {
                        return 0;
                    } else {
                        temp += (int) obj;
                    }
                }
                if (stack.isEmpty()) {
                    return 0;
                }
                stack.pop();
                if (temp == 0) {
                    stack.push(3);
                } else {
                    stack.push(3 * temp);
                }
            }
        }

        int result = 0;
        while (!stack.isEmpty()) {
            Object obj = stack.pop();
            if (obj instanceof String) {
                return 0;
            }
            result += (int) obj;
        }
        return result;

    }

}
