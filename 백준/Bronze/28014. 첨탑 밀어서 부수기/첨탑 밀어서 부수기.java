import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int h = 0;
        int left = 0;
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            h = Integer.parseInt(st.nextToken());
            if (left <= h)
                cnt++;
            left = h;
        }

        System.out.println(cnt);

    }
}
