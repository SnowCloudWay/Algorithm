import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        while(true) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int age = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            if (name.equals("#") && age == 0 && weight == 0)
                break;
            sb.append(name).append(" ");
            if (age > 17 || weight >= 80)
                sb.append("Senior");
            else
                sb.append("Junior");
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
