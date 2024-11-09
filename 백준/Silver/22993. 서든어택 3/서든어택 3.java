import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long jun = Long.parseLong(st.nextToken());
        boolean live = true;

        ArrayList<Long> arr = new ArrayList<>();
        for (int i = 0; i < n-1; i++) arr.add(Long.parseLong(st.nextToken()));
        Collections.sort(arr);

        for (long a : arr) {
            if (jun > a) jun += a;
            else {
                live = false;
                break;
            }
        }

        System.out.println(live ? "Yes" : "No");

    }

}
