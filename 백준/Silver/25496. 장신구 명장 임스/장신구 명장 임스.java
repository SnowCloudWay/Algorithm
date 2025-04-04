import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int cnt = 0;
        int p = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] A = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            A[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(A);
        
        if (p < 200) {
            for (int i = 0; i < N; i++) {
                p += A[i];
                cnt++;
                if (p >= 200)
                    break;
            }
        }

        System.out.println(cnt);

    }
}
