import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Map<String, Integer> map = new HashMap<>();
        map.put("STRAWBERRY", 0);
        map.put("BANANA", 0);
        map.put("LIME", 0);
        map.put("PLUM", 0);

        boolean bell = false;

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String fruit = st.nextToken();
            map.put(fruit, map.get(fruit) + Integer.parseInt(st.nextToken()));
        }

        for (String key : map.keySet()) {
            if (map.get(key) == 5) {
                bell = true;
                break;
            }
        }

        System.out.println(bell ? "YES" : "NO");

    }
}
