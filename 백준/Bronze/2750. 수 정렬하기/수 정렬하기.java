import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> nums = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(nums);

        for (int num : nums) {
            System.out.println(num);
        }

    }

}
