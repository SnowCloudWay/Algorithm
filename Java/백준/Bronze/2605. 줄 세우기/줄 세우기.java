import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        ArrayList<Integer> result = new ArrayList<>();

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++)
            result.add(i-Integer.parseInt(st.nextToken()), i+1);

        for (int r : result)
            sb.append(r).append(" ");

        System.out.println(sb);

    }
}
