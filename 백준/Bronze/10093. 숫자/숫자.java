import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        if (a < b) {
            System.out.println(b - a - 1);
            for (long i = a+1; i < b; i++)
                sb.append(i).append(" ");
            System.out.println(sb);
        } else if (a > b) {
            System.out.println(a - b - 1);
            for (long i = b+1; i < a; i++)
                sb.append(i).append(" ");
            System.out.println(sb);
        } else {
            System.out.println(0);
        }

    }
}