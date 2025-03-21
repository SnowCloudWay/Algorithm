import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        ArrayList<String> words;

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            words = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens())
                words.add(st.nextToken());
            sb.append(String.format("Case #%d: ", i+1));
            for (int j = words.size()-1; j >= 0; j--)
                sb.append(words.get(j)).append(" ");
            sb.append("\n");
        }
        
        System.out.println(sb);
        
    }
}