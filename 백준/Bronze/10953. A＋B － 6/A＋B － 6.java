import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());


        for (int i = 0; i < n; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine(), ",");
            int a = Integer.parseInt(str.nextToken());
            int b = Integer.parseInt(str.nextToken());
            int sum = a + b;
            System.out.println(sum);
        }


    }
}
