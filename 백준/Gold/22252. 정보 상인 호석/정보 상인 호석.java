import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        HashMap<String, PriorityQueue<Integer>> map = new HashMap<>();
        long total = 0;

        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            long k = Long.parseLong(st.nextToken());
            if (num == 1) {
                if (!map.containsKey(name))
                    map.put(name, new PriorityQueue<>(Collections.reverseOrder()));
                for (long j = 0; j < k; j++)
                    map.get(name).offer(Integer.parseInt(st.nextToken()));
            } else {
                if (map.containsKey(name)) {
                    if (map.get(name).size() < k)
                        k = map.get(name).size();
                    for (long j = 0; j < k; j++)
                        total += map.get(name).poll();
                }
            }
        }
        System.out.println(total);
    }
}
