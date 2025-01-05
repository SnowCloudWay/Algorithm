import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        HashMap<String, Integer> dict = new HashMap<>();

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            dict.put(st.nextToken(), 0);

        st = new StringTokenizer(br.readLine());
        String str = "";
        for (int i = 0; i < N - 1; i++) {
            str = st.nextToken();
            dict.put(str, dict.get(str) + 1);
        }

        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            if (entry.getValue() == 0) {
                System.out.println(entry.getKey());
                break;
            }
        }

    }
}
