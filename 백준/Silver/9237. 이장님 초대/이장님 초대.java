import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int maxDay = 0;
        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        Integer[] nums = new Integer[n];
        for (int i = 0; i < n; i++)
            nums[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(nums, Collections.reverseOrder());

        for (int i = 0; i < n; i++)
            if (nums[i] + i + 2 > maxDay)
                maxDay = nums[i] + i + 2;

        System.out.println(maxDay);

    }
}
