import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int cnt = 0;

        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            nums[i] = Integer.parseInt(st.nextToken());

        for (int i = 1; i < N; i++) {
            if (nums[i] <= nums[i-1]) {
                nums[i] += K;
                cnt++;
            }
            if (nums[i] <= nums[i-1]) {
                cnt = -1;
                break;
            }
        }

        System.out.println(cnt);

    }
}
