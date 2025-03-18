import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Integer> stack = new Stack<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++)
            stack.add(Integer.parseInt(br.readLine()));

        int last = stack.get(stack.size() - 1);
        int cnt = 1;
        for (int i = stack.size() - 1; i >= 0; i--) {
            if (stack.get(i) > last) {
                last = stack.get(i);
                cnt++;
            }
        }

        System.out.println(cnt);

    }
}
