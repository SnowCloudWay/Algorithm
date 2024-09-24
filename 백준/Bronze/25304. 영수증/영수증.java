import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int money = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int total = 0;

        for(int i = 0; i < n; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int price = Integer.parseInt(str.nextToken());
            int quantity = Integer.parseInt(str.nextToken());
            total += price * quantity;
        }

        if(money == total)
            System.out.println("Yes");
        else
            System.out.println("No");

    }

}
