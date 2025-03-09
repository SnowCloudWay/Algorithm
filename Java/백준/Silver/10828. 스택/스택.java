import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        Stack<Integer> stackInt = new Stack<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "push":
                    stackInt.push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    if (!stackInt.empty()) sb.append(stackInt.pop());
                    else sb.append(-1);
                    sb.append("\n");
                    break;
                case "size":
                    sb.append(stackInt.size()).append("\n");
                    break;
                case "empty":
                    if (stackInt.empty()) sb.append(1);
                    else sb.append(0);
                    sb.append("\n");
                    break;
                case "top":
                    if (!stackInt.empty()) sb.append(stackInt.peek());
                    else sb.append(-1);
                    sb.append("\n");
                    break;
                default:
                    break;
            }
        }

        System.out.println(sb);

    }
}