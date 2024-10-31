import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            Stack<String> stackStr = new Stack<>();
            String s = br.readLine();

            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c == '(') {
                    stackStr.push(String.valueOf(c));
                } else {
                    if (!stackStr.isEmpty() && stackStr.peek().equals("(")) {
                        stackStr.pop();
                    } else {
                        stackStr.push(String.valueOf(c));
                        break;
                    }
                }
            }

            if (stackStr.isEmpty()) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }

    }

}
