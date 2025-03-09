import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        Deque<Integer> que = new ArrayDeque<>();
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "push":
                    que.offer(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    if (!que.isEmpty()) sb.append(que.poll());
                    else sb.append(-1);
                    sb.append("\n");
                    break;
                case "size":
                    sb.append(que.size()).append("\n");
                    break;
                case "empty":
                    if (!que.isEmpty()) sb.append(0);
                    else sb.append(1);
                    sb.append("\n");
                    break;
                case "front":
                    if (!que.isEmpty()) sb.append(que.peek());
                    else sb.append(-1);
                    sb.append("\n");
                    break;
                case "back":
                    if (!que.isEmpty()) sb.append(que.peekLast());
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